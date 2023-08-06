![Logo](https://github.com/engie-group/shaystack/blob/develop/docs/logo.png?raw=true)

# Shift-4-Haystack

## About Haystack, and who is it for

[Haystack project]((https://project-haystack.org/)) is an open source initiative to standardize semantic data models for
Internet Of Things. It enables interoperability between any IoT data producer and consumer, mainly in the Smart Building
area.

Haystack core data model is the Grid, it can be serialized in many formats,
mainly [Zinc](https://www.project-haystack.org/doc/docHaystack/Zinc),
[Trio](https://www.project-haystack.org/doc/docHaystack/Trio),
[Json](https://www.project-haystack.org/doc/docHaystack/Json)
and [Csv](https://www.project-haystack.org/doc/docHaystack/Csv)

## About this project

This project implements client side haystack code. Useful to parse or dump Haystack files
([Zinc](https://www.project-haystack.org/doc/docHaystack/Zinc),
[Trio](https://www.project-haystack.org/doc/docHaystack/Trio),
[Json](https://www.project-haystack.org/doc/docHaystack/Json),
[Csv](https://www.project-haystack.org/doc/docHaystack/Csv)).

On the server side, it also implements [Haystack Rest API](https://project-haystack.org/doc/docHaystack/HttpApi), useful
to serve Haystack data you host.

- [Try it with colab?](https://colab.research.google.com/github/pprados/shaystack/blob/develop/haystack.ipynb)
- [Try it with AWS Lambda?](https://skz7riv2yk.execute-api.us-east-2.amazonaws.com/dev)

The [full documentation is here](https://engie-group.github.io/shaystack/)
and the [documentation of API is here](https://engie-group.github.io/shaystack/api/shaystack/index.html)
