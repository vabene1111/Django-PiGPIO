action "Django Test" {
  uses = "vabene1111/django-test-action@master"
}

workflow "Run Tests Manual" {
  resolves = ["Django Test"]
  on = "check_run"
}
