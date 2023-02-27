WITH Fibonacci(iter,a,number,b) AS
(
 SELECT iter=1, a=1, number=1, b=1+1
 UNION ALL
 SELECT iter+1, a=number, number=b, b=number+b
 FROM Fibonacci WHERE iter < 91
)
SELECT iter, number FROM Fibonacci;