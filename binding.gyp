{
  "targets": [
    {
      "target_name": "calculator",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [
            "./src/sorting-algos/heap-sort/heap-sort.cpp",
            "./src/sorting-algos/heap-sort/index.cpp"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    }
  ]
}