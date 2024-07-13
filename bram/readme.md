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

- [ ] Get rid of string intermediary everywhere
- [ ] Make my behavior optional
- [ ] Integrate something like FastAPI into the mix, why not. 
- [ ] Why not `textual` > `rich`?
  - It's a totally unnecessary over complication, my whole point is that a certain kind of TUI and CLI are kind of interchangeable. And maybe that so it also goes for an API. 
  - Does textual e.g. work over ssh?