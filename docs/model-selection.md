

| Model | Acc | Recall ES1 | Macro F1 | Train (seconds) | Infer | Explain |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| LogReg(baseline) | 0.671 | 0.250 | 0.492 | 19.980 | 0.003 | High |
| Random Forest (Untuned) | 0.638	 | 0.000	 | 0.384 | 62.574 | 0.137 | Medium |
| Random Forest (Tuned) | 0.610 | 0.312	 | 0.476 | 381.502	 | 0.105 | Medium |
| Gradient Boosting | 0.550	 | 0.312 | 0.417 | 12.054	 | 0.022 | Low |
| MLP Small Neural Network | 0.634 | 0.188	 | 0.471 | 281.323	 | 0.005 | Low |

