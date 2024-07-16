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
- [ ] `ValidationError` and the like
  - [x] `_convert` -- python ./bram/recycle.py literal 42

What then?

- [ ] Make my behavior optional
- [ ] Do calls deeper into the library (if I'm slowing things down)
- [ ] Make a recycled FastAPI demo (or similar, I want to think of a way to support multiple kinds of output). 
- [ ] Why not `textual` > `rich`?
    - It's a totally unnecessary over complication.
    - It doesn't map at all as nice onto CLIs as most TUIs.
    - But it does work over ssh and is probably way nicer to use??