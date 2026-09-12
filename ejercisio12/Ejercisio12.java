package com.mycompany.ejercisio12;

import java.util.Scanner;

public class Ejercisio12 {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        double metros;
        double centimetros;
        double pulgadas;
        double pies;
        double yardas;

        System.out.print("Ingrese la cantidad de metros: ");
        metros = teclado.nextDouble();

        // Conversiones
        centimetros = metros * 100;
        pulgadas = centimetros / 2.54;
        pies = pulgadas / 12;
        yardas = pies / 3;

        // Resultados
        System.out.println("Cantidad de metros: " + metros);
        System.out.println("Centimetros: " + centimetros);
        System.out.println("Pulgadas: " + pulgadas);
        System.out.println("Pies: " + pies);
        System.out.println("Yardas: " + yardas);
    }
}