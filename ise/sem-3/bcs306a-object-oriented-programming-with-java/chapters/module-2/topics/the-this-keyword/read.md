java
class Student {
String name;
int usn;

    void setData(String name, int usn) {
        name = name;        // Which 'name' is which? The parameter is assigned to itself.
        usn = usn;          // The instance variable 'usn' remains unchanged (probably 0).
    }

}
