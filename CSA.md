# Configuration Status Accounting (CSA) Record

Project: Inventory Tracker (SEN 401, Lab 3)
Author: Emmanuel Oyebanji Oyebode (2024/C/SENG/0866)

## Configuration items

| Item | Description |
|---|---|
| `inventory.py` | Item data model and stock list |
| `app.py` | Stock report and total stock value |
| `utils/helpers.py` | Highest/lowest stock item, money formatting |
| `requirements.txt` | Dependencies (standard library only) |
| `README.md` | Project description and instructions |
| `changelog.txt` | Exported commit log (hash, author, date, message) |

## Branches

| Branch | Purpose | Status |
|---|---|---|
| `main` | Released code | Contains release v1.0 |
| `dev` | Maintenance work | Merged into `main` |

## Releases

| Tag | Commit | Description |
|---|---|---|
| `v1.0` | c6b7ce4 | Inventory tracker after all four maintenance tasks |

## Commits mapped to maintenance tasks

| Commit | Type | Change |
|---|---|---|
| 4702ec2 | Baseline | Initial commit: README and requirements |
| c37779d | Baseline | Add inventory.py |
| 313ca4b | Baseline | Add helper functions |
| d8acaa6 | Baseline | Add app.py |
| fb45244 | Corrective | Total stock value used `+` instead of `*`; lowest_stock_item compared with `>` |
| a5f1c08 | Adaptive | Dataclass `Item`, modern type hints, low stock alert, `__main__` guard |
| faaa99a | Perfective | Formatted table with values in Naira, out-of-stock highlighting |
| 4cd3f38 | Preventive | Smaller documented functions, `Item.value`, `money()` helper, constants |
| c6b7ce4 | Release | Merge `dev` into `main`, tagged v1.0 |

## Commands used

```bash
git log --oneline
git log --oneline --graph --decorate --all
git branch -a
git tag -n
git log --pretty=format:"%h | %an | %ad | %s" --date=format:"%Y-%m-%d %H:%M" --output=changelog.txt
```
