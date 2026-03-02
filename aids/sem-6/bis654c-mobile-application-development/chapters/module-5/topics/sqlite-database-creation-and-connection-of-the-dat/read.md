java
    public final class FeedReaderContract {
        private FeedReaderContract() {} // To prevent someone from instantiating the contract class

        public static class FeedEntry implements BaseColumns {
            public static final String TABLE_NAME = "entry";
            public static final String COLUMN_NAME_TITLE = "title";
            public static final String COLUMN_NAME_SUBTITLE = "subtitle";
        }
    }