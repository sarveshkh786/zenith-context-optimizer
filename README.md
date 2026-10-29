# 🎯 Zenith Context Optimizer

**Authored by Sarvesh Zenith (Sarvesh Khandelwal) | Dayal Infotech Services**

`zenith-context-optimizer` is an intelligent, high-performance context window management and token pruning engine built for agentic AI architectures and Multi-Agent Swarms.

---

## ✨ Key Features
- ⚡ **Dynamic Token Pruning**: Intelligently prunes conversation history while preserving system instructions and core context.
- 📐 **Tiktoken Integration**: Fast token estimation compatible with OpenAI, Anthropic, and open-source models.
- 🔄 **Agentic Memory Optimization**: Maximizes signal-to-noise ratio in model prompts for long-running workflows.

---

## 🚀 Quickstart

```python
from optimizer import ContextOptimizer

optimizer = ContextOptimizer(model_name="gpt-4", max_tokens=2048)

messages = [
    {"role": "system", "content": "You are Zenith Context Optimizer AI Assistant."},
    {"role": "user", "content": "Hello, can you help me optimize context windows?"}
]

optimized_messages = optimizer.prune_context(messages)
print(optimized_messages)
```
