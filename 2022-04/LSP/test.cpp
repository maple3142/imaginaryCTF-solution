#define flag
#define ictf

template<typename T>
void f(T x){

}

int main(){
    f<(
#include "/app/flag.txt"
)>(1);
    return 0;
}
