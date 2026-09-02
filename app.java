import java.util.Scanner;

public class SimpleJavaProgram {
    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine().trim(); // Read and trim input

        // Validate input
        if (name.isEmpty()) {
            System.out.println("You didn't enter a name!");
        } else {
            System.out.println("Hello, " + name + "! Welcome to Java.");
        }

        scanner.close(); // Close the scanner to avoid resource leaks
    }
}

