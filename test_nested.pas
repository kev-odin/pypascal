PROGRAM nested;
VAR
   a : INTEGER;

PROCEDURE P1;
VAR
   a : REAL;
   k : INTEGER;

   PROCEDURE P2;
   VAR
      a, z : INTEGER;
   BEGIN
      z := 777;
   END;

BEGIN

END;

BEGIN
   a := 10;
END.