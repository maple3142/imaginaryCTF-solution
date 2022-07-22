function readn(heap, ptr, n){
	let s1 = ''
	let s2 = ''
	let stop = false
	for(let i = 0; i < n; i++){
		if(!heap[ptr+i]) stop = true
		if(!stop) s1 += String.fromCharCode(heap[ptr + i])
		s2 += heap[ptr + i].toString(16).padStart(2, '0')
	}
	return [s1, s2]
}
;(async () => {
	delete require.cache[require.resolve('./main.js')]
	const Module = require('./main.js')
	const ready = new Promise(function (res) {
		Module.onRuntimeInitialized = res
	})
	await ready
	const nums = process.argv.slice(2).map(x=>parseInt(x, 16))
	const s = nums.map(x=>String.fromCharCode(x)).join('')
	console.log(s)
	const l = Module.intArrayFromString(s)
	const r = Module._base64_encode(Module.allocate(l, 0), s.length / 2)
	const [s1, s2] = readn(Module.HEAPU8,r, 256)
	console.log(...nums)
	console.log(s1)
	console.log(s2)
	console.log(atob(s1))
})()
