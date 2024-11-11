It is also known as Input Space
Partitioning (ISP). It is a black-box testing technique where
the input domain of the system under test is divided into
distinct groups that are expected to exhibit similar behavior.
Instead of testing each input individually, one test case is
selected from each partition assumes that all inputs in the
same partition will behave similarly. In other words that one
test acts as a representative of all the other partitions without
sacrificing coverage. For manually generating partition test
cases we follow the following steps:
• Determine the range or set of possible inputs for the
system.
• Group inputs into partitions where the system is expected
to behave similarly
• Choose representative test cases from each partition.
• Run tests using the selected test cases in TDD cycle and
evaluate the results.
It has several advantages over other test generation methods.
Partition testing allows for fewer test cases compared to
Fig. 3. State transition test cases
exhaustive testing, making it more efficient without significant
loss of coverage. It also provides a structured way to select
test cases, ensuring each part of the input space is covered
without redundancy. It helps testers focus on critical inputs,
especially where the behavior of the system is most likely to
differ, which covers the major task of boundary value analysis.
The only challenge with partition testing is that in order to
effectively create partitions, it often requires deep knowledge
of the problem domain.
