# Query Review Checklist

- inspect indexes before rewriting large queries blindly
- check whether access patterns and schema shape match the SQL being written
- treat RLS and locking as correctness constraints, not optional extras
- prefer evidence from plans or metrics over intuition alone
