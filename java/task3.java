public class task3 {
    
    public static void main(String[] args) {
        String name = "name";

        // Potential bugs: What if when running program, there is no arguments given
        // Set a default value for name and only insert name if given
        if (args.length != 0)
            name = args[0];

        System.out.println("Hello, " + name + "!");
    }
}