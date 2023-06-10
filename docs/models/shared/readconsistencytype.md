# ReadConsistencyType

* `majority` - send N/2+1 random request and return points, which present on all of them

* `quorum` - send requests to all nodes and return points which present on majority of nodes

* `all` - send requests to all nodes and return points which present on all nodes


## Values

| Name       | Value      |
| ---------- | ---------- |
| `MAJORITY` | majority   |
| `QUORUM`   | quorum     |
| `ALL`      | all        |