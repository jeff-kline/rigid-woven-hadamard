// Fixed TD(4,20) from F4 x F5 and a Paley basis. No sign search.
import assert from 'node:assert/strict';

const h = 20, k = 4, n = k*h*h;
const range = length => Array.from({length}, (_, i) => i);
const multiply4 = [[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]];
const slopes = [null,0,2,3]; // same integer representatives in the two fields
function direction(i, a, b) {
  if (slopes[i] === null) return b;
  const x = Math.floor(a/5) ^ multiply4[slopes[i]][Math.floor(b/5)];
  const y = (a%5 + slopes[i]*(b%5))%5;
  return 5*x+y;
}
const lineJoin = range(k).map(() => range(k).map(() => new Int16Array(h*h).fill(-1)));
const point = range(k).map(() => new Uint8Array(h*h));
const port = range(k).map(() => new Uint8Array(h*h));
for (let a=0; a<h; a++) for (let b=0; b<h; b++) {
  const l = h*a+b;
  for (let i=0; i<k; i++) {
    point[i][l] = direction(i,a,b);
    port[i][l] = direction(i,b,a);
  }
  for (let i=0; i<k; i++) for (let j=0; j<k; j++) {
    const s = point[i][l], r = i===j ? port[i][l] : point[j][l];
    assert.equal(lineJoin[i][j][h*s+r], -1);
    lineJoin[i][j][h*s+r] = l;
  }
}
for (const groups of lineJoin) for (const pair of groups) assert(pair.every(l => l>=0));
const squares = new Set(range(18).map(i => ((i+1)**2)%19));
const A = range(h).map(a => range(h).map(b => {
  if (a===b || a===0) return 1;
  if (b===0) return -1;
  return squares.has((19+b-a)%19) ? 1 : -1;
}));
for (let a=0; a<h; a++) for (let b=0; b<=a; b++)
  assert.equal(A[a].reduce((sum, v, i) => sum+v*A[b][i],0), a===b?h:0);
const K = [[0,1,1,1],[-1,0,1,-1],[-1,-1,0,1],[-1,1,-1,0]];
const d = [-1,1,1,1];
const width = Math.ceil(n/32);
const rows = range(n).map(() => new Uint32Array(width));
const colSums = new Int32Array(n);
for (let i=0; i<k; i++) for (let s=0; s<h; s++) for (let a=0; a<h; a++) {
  const row = rows[(i*h+s)*h+a];
  let rowSum = 0;
  for (let j=0; j<k; j++) for (let r=0; r<h; r++) {
    const l = lineJoin[i][j][s*h+r];
    const first = A[a][port[i][l]], secondPort = i===j ? s : port[j][l];
    const c = i===j ? 1 : K[i][j];
    const scalar = A[a][s]*c*first*d[j];
    for (let b=0; b<h; b++) {
      const col = (j*h+r)*h+b;
      const value = scalar*A[b][secondPort]*A[b][r];
      assert(value===1 || value===-1);
      if (value<0) row[col>>>5] |= 1<<(col%32);
      colSums[col] += value;
      rowSum += value;
    }
  }
  assert.equal(rowSum,2*h);
}
assert(colSums.every(v => v===2*h));
function popcount(x) {
  x -= (x>>>1)&0x55555555;
  x = (x&0x33333333)+((x>>>2)&0x33333333);
  return (((x+(x>>>4))&0x0f0f0f0f)*0x01010101)>>>24;
}
for (let i=0; i<n; i++) for (let j=0; j<i; j++) {
  let distance = 0;
  for (let w=0; w<width; w++) distance += popcount(rows[i][w]^rows[j][w]);
  assert.equal(distance,n/2);
}
console.log('Regular order 1600: all 2560000 sign entries checked; all row and column sums 40; all 1279200 row-pair distances 800.');
