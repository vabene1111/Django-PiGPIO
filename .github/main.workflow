workflow "Run Tests" {
  on = "push"
  resolves = ["Django Test"]
}

action "Django Test" {
  uses = "vabene1111/django-test-action"
}
