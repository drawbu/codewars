{
  description = "My codewars solutions";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      with import nixpkgs { inherit system; }; {
        devShells.default = mkShell {
          packages = [
            criterion
            gcovr
            gcc12
            gnumake
            man
            python311
          ];
        };
      });
}
