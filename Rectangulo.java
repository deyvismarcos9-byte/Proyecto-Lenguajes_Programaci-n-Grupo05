package proyecto.ejercicio2;

import java.util.Scanner;

public class Rectangulo {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        double base;
        double altura;
        double area;

        System.out.print("Ingrese la base: ");
        base = teclado.nextDouble();

        System.out.print("Ingrese la altura: ");
        altura = teclado.nextDouble();

        area = base * altura;

        System.out.println("El area del rectangulo es: " + area);
    }
}