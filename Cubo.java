package proyecto.ejercicio1;

import java.util.Scanner;

public class Cubo {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        double numero;
        double resultado;

        System.out.print("Ingrese un numero: ");
        numero = teclado.nextDouble();

        resultado = numero * numero * numero;

        System.out.println("El cubo del numero ingresado es: " + resultado);
    }
}