PRAGMA foreign_key = ON;

CREATE TABLE nodes (
    id TEXT PRIMARY KEY NOT NULL,
    properties TEXT                  -- JSON BLOB
);


CREATE TABLE edges (
   from_node TEXT NOT NULL,
   to_node TEXT NOT NULL,
   rel_type TEXT NOT NULL,
   properties TEXT,

   FOREIGN KEY (from_node) REFERENCES node(id),
   FOREIGN KEY (to_node) REFERENCES node(id),
   UNIQUE(from_node,to_node,rel_type)

);