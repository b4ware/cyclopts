I'm taking notes too many places.

```sh
poetry shell
python ./bram/recycle.py
```

Where I have a rich.prompt thing:

- [x] `MissingArgumentError` 
  - [x] `create_bound_arguments()` -- python ./bram/recycle.py literal
    - [ ] Get rid of whole function re-calls
    - [ ] Offer infinite retries
- [ ] `ValidationError`
- [ ] `CoercionError`

What then?

- [ ] Make my behavior optional
- [ ] Do calls deeper into the library (if I'm slowing things down)
- [ ] Make a recycled FastAPI demo (or similar, I want to think of a way to support multiple kinds of output). 
- [ ] Why not `textual` > `rich`?
  - It's a totally unnecessary over complication, my whole point is that a certain kind of TUI and CLI are kind of interchangeable.
  - Does textual e.g. work over ssh?