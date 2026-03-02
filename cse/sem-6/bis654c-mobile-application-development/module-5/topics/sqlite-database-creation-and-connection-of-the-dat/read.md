java
public class DatabaseHelper extends SQLiteOpenHelper {

// Database Info
private static final String DATABASE_NAME = "notesDatabase";
private static final int DATABASE_VERSION = 1;

// Table Name
public static final String TABLE_NOTES = "notes";

// Column Names
public static final String KEY_ID = "id";
public static final String KEY_NOTE = "note";

public DatabaseHelper(Context context) {
super(context, DATABASE_NAME, null, DATABASE_VERSION);
}

@Override
public void onCreate(SQLiteDatabase db) {
String CREATE_NOTES_TABLE = "CREATE TABLE " + TABLE_NOTES +
"(" +
KEY_ID + " INTEGER PRIMARY KEY AUTOINCREMENT," +
KEY_NOTE + " TEXT" +
")";
db.execSQL(CREATE_NOTES_TABLE);
}

@Override
public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
if (oldVersion != newVersion) {
// Simplest strategy: drop and recreate
db.execSQL("DROP TABLE IF EXISTS " + TABLE_NOTES);
onCreate(db);
}
}

}
