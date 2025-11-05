import java.util.*;

public class task4 {

    static class Person implements Comparable<Person> {
        final String first;
        final String last;
        final int age;
        Person(String first, String last, int age) {
            this.first = first; this.last = last; this.age = age;
        }
        public int getAge(){
            return this.age;
        }
        public String getFirstName(){
            return this.first;
        }
        public String getLastName(){
            return this.last;
        }
        @Override public String toString() {
            return last + ", " + first + " (" + age + ")";
        }
        @Override public int compareTo(Person other) {
            return this.last.compareTo(other.last);
        }
    }

    public static void main(String[] args) {
        Person[] people = new Person[] {
            new Person("Ben", "Adams", 30),
            new Person("Ana", "Zhang", 22),
            new Person("Cara", "Lopez", 27),
            new Person("Ben", "Adams", 35)
        };
        
        // Sort by last name ascending
        Arrays.sort(people);
        // Sort by age descending then first ascending
        Arrays.sort(people, Comparator.comparingInt(Person::getAge).reversed().thenComparing(Person::getFirstName));
        for (Person p : people) System.out.println(p);
    }
}
