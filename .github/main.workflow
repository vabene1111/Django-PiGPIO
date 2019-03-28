workflow "Run Tests" {
  resolves = ["Django Test"]
  on = "push"
}

action "Django Test" {
  uses = "vabene1111/django-test-action@master"
}
