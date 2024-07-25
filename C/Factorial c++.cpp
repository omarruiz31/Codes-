#include <iostream>

// Función recursiva para calcular el factorial
int factorial(int n) {
    // Caso base: factorial de 0 es 1
    if (n == 0)
        return 1;
    // Caso recursivo: n * factorial(n-1)
    else
        return n * factorial(n - 1);
}

int main() {
    int num;
    std::cout << "Ingrese un numero para calcular su factorial: ";
    std::cin >> num;

    // Verificación para números negativos
    if (num < 0)
        std::cout << "No se puede calcular el factorial de un número negativo.\n";
    else {
        int fact = factorial(num);
        std::cout << "El factorial de " << num << " es: " << fact << "\n";
    }

    return 0;
}
