/*
 * Needlepoint Studio unlocker (service worker).
 *
 * The published app is encrypted (<file>.enc). After the passphrase page stores
 * a key on this device, this worker decrypts each app file as the browser asks
 * for it. Without a valid key it sends visitors back to the passphrase page.
 */
const SCOPE = self.registration.scope
const SCOPE_PATH = new URL(SCOPE).pathname
const PUBLIC = new Set(['', 'index.html', 'sw.js', 'manifest.json'])

self.addEventListener('install', () => self.skipWaiting())
self.addEventListener('activate', (e) => e.waitUntil(self.clients.claim()))

let manifestPromise = null
function manifest(fresh) {
  if (fresh || !manifestPromise) {
    manifestPromise = fetch(SCOPE + 'manifest.json', { cache: 'no-cache' }).then((r) => r.json())
    manifestPromise.catch(() => { manifestPromise = null })
  }
  return manifestPromise
}

function savedKey() {
  return new Promise((resolve) => {
    const open = indexedDB.open('npstudio-lock', 1)
    open.onupgradeneeded = () => open.result.createObjectStore('keys')
    open.onerror = () => resolve(null)
    open.onsuccess = () => {
      const tx = open.result.transaction('keys', 'readonly')
      const get = tx.objectStore('keys').get('current')
      get.onsuccess = () => resolve(get.result || null)
      get.onerror = () => resolve(null)
    }
  })
}

const toGate = () => Response.redirect(SCOPE + '?locked', 302)

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url)
  if (e.request.method !== 'GET' || !url.href.startsWith(SCOPE)) return
  const rel = decodeURIComponent(url.pathname.slice(SCOPE_PATH.length))
  if (PUBLIC.has(rel) || rel.endsWith('.enc')) return
  e.respondWith(serve(rel, e.request))
})

async function serve(rel, request) {
  let m = await manifest(request.mode === 'navigate')
  let type = m.files[rel]
  if (!type) {
    m = await manifest(true) // a newer build may have been published
    type = m.files[rel]
    if (!type) return fetch(request)
  }
  const saved = await savedKey()
  if (!saved || saved.salt !== m.salt) return toGate()
  const res = await fetch(SCOPE + rel + '.enc', { cache: 'no-cache' })
  if (!res.ok) return new Response('Not found', { status: 404 })
  const buf = new Uint8Array(await res.arrayBuffer())
  try {
    const plain = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: buf.slice(0, 12) }, saved.key, buf.slice(12))
    return new Response(plain, { headers: { 'Content-Type': type, 'Cache-Control': 'no-store' } })
  } catch {
    return toGate()
  }
}
