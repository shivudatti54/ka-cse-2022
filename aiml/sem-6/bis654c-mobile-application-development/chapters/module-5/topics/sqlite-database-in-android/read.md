java
public final class StudentContract {
    private StudentContract() {} // To prevent instantiation

    public static class StudentEntry implements BaseColumns {
        public static final String TABLE_NAME = "students";
        public static final String COLUMN_NAME = "name";
        public static final String COLUMN_USN = "usn";
        public static final String COLUMN_SEM = "semester";
    }
}