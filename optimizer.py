"""
Zenith Context Optimizer
Author: Sarvesh Zenith (Sarvesh Khandelwal) - Dayal Infotech Services
"""

import tiktoken

class ContextOptimizer:
    def __init__(self, model_name: str = "gpt-4", max_tokens: int = 4096):
        self.model_name = model_name
        self.max_tokens = max_tokens
        try:
            self.encoding = tiktoken.encoding_for_model(model_name)
        except Exception:
            self.encoding = tiktoken.get_encoding("cl100k_base")

    def count_tokens(self, text: str) -> int:
        return len(self.encoding.encode(text))

    def prune_context(self, messages: list[dict], target_max_tokens: int = None) -> list[dict]:
        limit = target_max_tokens or self.max_tokens
        pruned = []
        current_tokens = 0
        
        # Keep system prompt if present
        system_msg = [m for m in messages if m.get("role") == "system"]
        other_msgs = [m for m in messages if m.get("role") != "system"]
        
        if system_msg:
            sys_tok = self.count_tokens(system_msg[0].get("content", ""))
            current_tokens += sys_tok
            pruned.extend(system_msg)
            
        # Process remaining messages in reverse (most recent first)
        for msg in reversed(other_msgs):
            tok = self.count_tokens(msg.get("content", ""))
            if current_tokens + tok <= limit:
                pruned.insert(1 if system_msg else 0, msg)
                current_tokens += tok
            else:
                break
                
        return pruned

if __name__ == "__main__":
    optimizer = ContextOptimizer(max_tokens=100)
    sample_msgs = [
        {"role": "system", "content": "You are Zenith Context Optimizer AI Assistant."},
        {"role": "user", "content": "Hello, can you help me optimize context windows?"},
        {"role": "assistant", "content": "Certainly! Context window optimization prunes redundant tokens while retaining vital prompt history."}
    ]
    optimized = optimizer.prune_context(sample_msgs)
    print("Optimized Context Messages count:", len(optimized))
