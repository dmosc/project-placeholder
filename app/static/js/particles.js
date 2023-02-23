import * as THREE from "https://unpkg.com/three@0.149.0/build/three.module.js";

/**
 * Globals.
 */
const scene = new THREE.Scene();

/**
 * Objects.
 */
const geometry = new THREE.BufferGeometry();
const material = new THREE.PointsMaterial({color: 0xf9f9f9});
const points = new THREE.Points(geometry, material);
const vertices = [];

for (let i = 0; i < 3000; ++i) {
  vertices.push(
    /*x=*/ THREE.MathUtils.randFloatSpread(200),
    /*y=*/ THREE.MathUtils.randFloatSpread(200),
    /*z=*/ THREE.MathUtils.randFloatSpread(200)
  );
}

geometry.setAttribute(
  "position",
  new THREE.Float32BufferAttribute(vertices, 3)
);

scene.add(points);

/**
 * Window configuration and scene visualization.
 */
const canvas = document.getElementById("background-canvas");
const sizes = {width: window.innerWidth, height: window.innerHeight};
const camera = new THREE.PerspectiveCamera(
  75,
  sizes.width / sizes.height,
  0.1,
  100
);
const renderer = new THREE.WebGLRenderer({canvas, alpha: true});

camera.position.set(0, 0, 10);
renderer.setSize(sizes.width, sizes.height);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

scene.add(camera);

window.addEventListener("resize", () => {
  sizes.width = window.innerWidth;
  sizes.height = window.innerHeight;
  camera.aspect = sizes.width / sizes.height;
  camera.updateProjectionMatrix();
  renderer.setSize(sizes.width, sizes.height);
  // Rendering optimization to limit pixel ratio
  // 2:1 virtual pixels to physical pixels.
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
});

/**
 * Animation cycle.
 */
let rotateFactor = 1;
document.getElementById("scrollable-section").addEventListener("scroll", () => {
  rotateFactor = 20;
  setTimeout(() => (rotateFactor = 1), 0);
});

(function tick() {
  const rotateCoeff = 0.1 * rotateFactor;
  points.rotateOnAxis(
    new THREE.Vector3(rotateCoeff, rotateCoeff, rotateCoeff),
    -0.001
  );
  renderer.render(scene, camera);
  window.requestAnimationFrame(tick);
})();
