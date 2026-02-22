# Interface Control Document (ICD): [Interface Name]

## 1. Description
Describe the interaction between Scope A and Scope B. What data or service is being exchanged?

## 2. Participating Scopes
- **Provider (Scope A)**: [e.g., Backend / Calculation Engine]
- **Consumer (Scope B)**: [e.g., Frontend / Configurator UI]

## 3. Data Interface / Contract
Define the "contract" that both sides agree to.

### Input Parameters (to Provider)
| Name | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| `pipe_id` | String | Unique identifier | Yes |
| `wt_params` | Object | Wall thickness inputs | Yes |

### Output Parameters (from Provider)
| Name | Type | Description | Format |
| :--- | :--- | :--- | :--- |
| `result_json` | JSON | Final calc results | [Link to Schema] |

## 4. Error Handling
How should errors be communicated between the scopes?

## 5. Versioning
Any changes to this interface must be versioned and approved by both scope leads.
- **Current Version**: 1.0.0
- **Approval Date**: [Date]
