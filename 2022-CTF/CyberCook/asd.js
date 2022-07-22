const Module = require('./main.js')
const ready = new Promise(function (res) {
	Module.onRuntimeInitialized = res
})
function readn(heap, ptr, n) {
	let s1 = ''
	let s2 = ''
	let stop = false
	for (let i = 0; i < n; i++) {
		if (!heap[ptr + i]) stop = true
		if (!stop) s1 += String.fromCharCode(heap[ptr + i])
		s2 += heap[ptr + i].toString(16).padStart(2, '0')
	}
	return [s1, s2]
}
function safechr(x) {
	if (x < 0x20) {
		return '.'
	}
	return String.fromCharCode(x)
}
function hexdump(mem, ptr, n) {
	let cnt = 0
	let s = ''
	let tmp = ''
	for (let i = 0; i < n; i++) {
		if (cnt === 0) {
			s += (ptr + i).toString(16).padStart(8, '0') + ': '
		}
		cnt += 1
		s += mem[ptr + i].toString(16).padStart(2, '0') + ' '
		tmp += safechr(mem[ptr + i])
		if (cnt >= 16) {
			s += '     ' + tmp
			s += '\n'
			tmp = ''
			cnt = 0
		}
	}
	console.log(s)
}
;(async () => {
	await ready
	// b64decode(bytes.fromhex('703650')+b'/') =  '\xa7\xa3\xff'
	// const s = '616263'.repeat(8) + 'a7a3ff'
	// const s = '616263'.repeat(10) + 'a7a3ff'
	const s = '3c696d672f7372632f6f6e6572726f723d6576616c28712e73293e787878' + 'a7a3ff'
	const l = Module.intArrayFromString(s)
	const ptr = Module.allocate(l, 0)
	console.log(ptr.toString(16))
	hexdump(Module.HEAPU8, ptr, 256)
	let r = Module._base64_encode(ptr, s.length / 2)
	console.log('r', r.toString(16))
	hexdump(Module.HEAPU8, ptr, 400)
})()
