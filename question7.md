Question 7
===
What is monkey patching and is it ever a good idea?

### Answer

Monkey patching is changing the behaviour of a function or object after it has already been defined. For example:
```python
import datetime
datetime.datetime.now = lambda: datetime.datetime(2012, 12, 12)
```
Most of the time it's a pretty terrible idea - it is usually best if things act in a well-defined way. One reason to monkey patch would be in testing. The mock package is very useful to this end.

## Why This Matters

It shows that you understand a bit about methodologies in unit testing. Your mention of monkey avoidance will show that you aren't one of those coders who favor fancy code over maintainable code (they are out there, and they suck to work with). Remember the principle of KISS? And it shows that you know a little bit about how Python works on a lower level, how functions are actually stored and called and suchlike.

**PS**: it's really worth reading a little bit about mock if you haven't yet. It's pretty useful.