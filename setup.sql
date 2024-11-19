CREATE TABLE IF NOT EXISTS task (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  summary VARCHAR(45),
  description TEXT,
  is_done BOOLEAN DEFAULT 0
);



-- optional create dummy date

INSERT INTO task (
  summary,
  description
) VALUES
(
  "walk the dog",
  "take fido out for a walk"
),
(
  "wash the car",
  "the car needs washing"
),
(
  "buy groceries",
  "we need milk, tomatoes, and bread"
);
