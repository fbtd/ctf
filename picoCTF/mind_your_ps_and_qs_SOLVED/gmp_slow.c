#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <gmp.h>

int main(void) {
    mpz_t c, n, e, b, a_square, b_square;
    mpz_init_set_str(c, "964354128913912393938480857590969826308054462950561875638492039363373779803642185", 10);
    mpz_init_set_str(n, "1584586296183412107468474423529992275940096154074798537916936609523894209759157543", 10);
    mpz_init_set_str(e, "65537", 10);

    mpz_init(b);
    mpz_init(a_square);
    mpz_init(b_square);
    mpz_set_ui(b, 3);
    mpz_set_ui(a_square, 123);  // whatever non-perfect square

    srand(time(NULL));
    while (!mpz_perfect_square_p(a_square)) {
        mpz_nextprime(b, b);
        mpz_mul(b_square, b, b );
        mpz_add(a_square, b_square, n);
    }
   gmp_printf("a square = %Zd\n", a_square);

    mpz_clear(c);
    mpz_clear(n);
    mpz_clear(e);
    mpz_clear(b);
    mpz_clear(a_square);
    mpz_clear(b_square);
}