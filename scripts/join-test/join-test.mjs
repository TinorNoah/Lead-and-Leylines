// Logs a bot into the local smoke-test server and times the join phases.
// Usage: node join-test.mjs [host] [port] [username]
// Exit 0 on spawn, 1 on kick/error/timeout. Prints one JSON line.
import mineflayer from 'mineflayer'

const host = process.argv[2] ?? '127.0.0.1'
const port = Number(process.argv[3] ?? '59969')
const username = process.argv[4] ?? 'join-test'
const timeoutMs = Number(process.env.JOIN_TEST_TIMEOUT_MS ?? '120000')

const t0 = Date.now()
const marks = {}
const mark = (name) => { marks[name] = Date.now() - t0 }

const done = (ok, extra = {}) => {
  console.log(JSON.stringify({ ok, host, port, username, ...marks, ...extra }))
  process.exit(ok ? 0 : 1)
}

const timer = setTimeout(() => done(false, { error: 'timeout waiting for spawn' }), timeoutMs)

let bot
try {
  bot = mineflayer.createBot({ host, port, username, version: '1.21.1' })
} catch (err) {
  clearTimeout(timer)
  done(false, { error: `createBot threw: ${err.message}` })
}

bot.once('login', () => mark('loginMs'))
bot.once('spawn', () => {
  mark('spawnMs')
  clearTimeout(timer)
  bot.chat('join-test ping')
  setTimeout(() => { bot.quit(); done(true) }, 2000)
})
bot.once('kicked', (reason) => {
  clearTimeout(timer)
  done(false, { error: `kicked: ${JSON.stringify(reason).slice(0, 500)}` })
})
bot.once('error', (err) => {
  clearTimeout(timer)
  done(false, { error: err.message.slice(0, 500) })
})
