package com.mycompany.ejercisio5;

import java.util.Scanner;

public class Ejercisio5 {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        double D, T, V;

        System.out.print("Ingrese la distancia (km): ");
        D = teclado.nextDouble();

        System.out.print("Ingrese el tiempo (h): ");
        T = teclado.nextDouble();

        V = D / T;

        System.out.println("La velocidad promedio es: " + V + " km/h");
    }
}