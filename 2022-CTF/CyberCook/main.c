#include "lib.h"
#include <stdio.h>

void f(){ return 0; }
u32 (*Z_envZ_emscripten_resize_heap)(u32) = f;
int main(){
    wasm_rt_init();
    Z_mainZ_init_conv();
    char* r = Z_mainZ_base64_encode("616263", 3);
    puts(r);
    wasm_rt_free();
    return 0;
}
