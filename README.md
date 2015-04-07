Docker Integration Test
===

# Repo Setup

The _test.py_ script will build the docker images and run their respective tests. Tests come in the form of another Dockerfile that is run ONTOP of the docker image you are wanting to test. You should not have to modify _test.py_ for this repo to work.

All configuration is done through _test.json_

This example repo stores all images in _1.5_ and all tests in _tests_

# Configuration

All images will be built according to _test.json_. This json object consists of the repository we are testing for, and the images we are running our tests on. They will be tagged: `repo:tag` where the tag belongs to the current image in the `tests` array. The `path` property tells _test.py_ where to find the Dockerfile to build the image, and the _test_ property tells _test.py_ where to find the Dockerfile to test our newly built image. If either the building of the image or the test fails, the entire build will fail.

# When / How to build

Uses [ghprb](https://github.com/janinko/ghprb). Excerpt from it's Readme:

This Jenkins plugin builds pull requests from GitHub and will report the results directly to the pull request via the GitHub Commit Status API

When a new pull request is opened in the project and the author of the pull request isn't whitelisted, builder will ask Can one of the admins verify this patch?. One of the admins can comment ok to test to accept this pull request for testing, test this please for one time test run and add to whitelist to add the author to the whitelist.

If an author of a pull request is whitelisted, adding a new pull request or new commit to an existing pull request will start a new build.

A new build can also be started with a comment: retest this please.

You can extend the standard build comment message on github creating a comment file from shell console or any other jenkins plugin. Contents of that file will be added to the comment on GitHub. This is usefull for posting some build dependent urls for users without access to the jenkins UI console.

Jobs can be configured to only build if a matching comment is added to a pull request. For instance, if you have two job you want to run against a pull request, a smoke test job and a full test job, you can configure the full test job to only run if someone adds the comment full test please on the pull request.
