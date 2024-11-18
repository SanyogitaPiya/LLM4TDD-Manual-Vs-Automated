Here is the conclusions and visualizations of manual tdd

Finding 1: While BVA and ISP testing offer general versatility, state transition testing is more effective in specialized contexts.

![image](https://github.com/user-attachments/assets/67dc67f3-d2d0-4043-8f3c-fda136456501)

Figure: Accuracy across difficulty

Finding 2: Test generation methods that focus on out-lining specific “important” inputs to focus on are more likely to provide better guidance as a prompt for code generation.

Finding 3: Boundary value analysis is the best choice for manual test generation to achieve accurate code. However, at large, manually generated test produce a high accuracy, although the number of prompts, and thus tests, varies.

![image](https://github.com/user-attachments/assets/b71b2076-48d9-412b-b83a-408b065d621e)

Finding 4: The performance of BVA within the LLM4TDD workflow benefits from the simpler problems that BVA can capture well. When applicable, decision tables and state transition testing have a good performance,
given the underlying complexity of the problems these test generation strategies can effectively capture.

Figure: Test to Prompt Ratio

![image](https://github.com/user-attachments/assets/3e37c86d-2ae7-4c04-834a-5e5e892f7653)

