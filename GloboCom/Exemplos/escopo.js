glob = 'global';

function a () {
  glob2 = 'global2';

  var loc1 = 'local';

  function () b {
    var loc2 = 'local2';
    // enxerga loc2, loc1, glob2, glob1
  }

  // nao enxerga loc2
  // enxerga loc1, glob2, glob1
}

// escopo global
// nao enxerga loc2, loc1
// enxerga glob2 depois de executar a()
// enxerga glob1
