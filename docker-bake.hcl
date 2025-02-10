group default {
  targets = ["api", "web"]
}

target api {
  dockerfile = "./deploy/api.dockerfile"
  tags = ["avatars_api"]
}

target web {
  dockerfile = "./deploy/web.dockerfile"
  tags = ["avatars_web"]
}
