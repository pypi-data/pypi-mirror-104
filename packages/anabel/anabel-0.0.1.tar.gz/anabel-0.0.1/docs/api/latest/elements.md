---
title: anabel.elements
summary: Element library
template: pdoc.html
...
<main>
<header>
<h1 class="title">Module <code>anabel.elements</code></h1>
</header>
<section id="section-intro">
<p>Element library</p>
</section>
<section>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="anabel.elements.BasicLink"><code class="flex name class">
<span>class <span class="ident">BasicLink</span></span>
<span>(</span><span>ndf, ndm, nodes)</span>
</code></dt>
<dd>
<div class="desc"><p>Class implementing general geometric element methods</p>
</div>
<h3>Subclasses</h3>
<ul class="hlist">
<li><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></li>
</ul>
<h3>Instance variables</h3>
<dl>
<dt id="anabel.elements.BasicLink.Dx"><code class="name">var <span class="ident">Dx</span> : float</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.BasicLink.Dy"><code class="name">var <span class="ident">Dy</span> : float</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.BasicLink.Dz"><code class="name">var <span class="ident">Dz</span> : float</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.BasicLink.L"><code class="name">var <span class="ident">L</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.BasicLink.L0"><code class="name">var <span class="ident">L0</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.BasicLink.Li"><code class="name">var <span class="ident">Li</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.BasicLink.cs"><code class="name">var <span class="ident">cs</span></code></dt>
<dd>
<div class="desc"><p>directional cosine</p>
</div>
</dd>
<dt id="anabel.elements.BasicLink.cz"><code class="name">var <span class="ident">cz</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.BasicLink.dofs"><code class="name">var <span class="ident">dofs</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.BasicLink.loc"><code class="name">var <span class="ident">loc</span> : jax._src.numpy.lax_numpy.ndarray</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.BasicLink.sn"><code class="name">var <span class="ident">sn</span> : float</code></dt>
<dd>
<div class="desc"><p>directional sine</p>
</div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="anabel.elements.BasicLink.Rx_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">Rx_matrix</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"><p>Rotation about x</p>
</div>
</dd>
<dt id="anabel.elements.BasicLink.Ry_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">Ry_matrix</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"><p>Rotation about z</p>
</div>
</dd>
<dt id="anabel.elements.BasicLink.Rz_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">Rz_matrix</span></span>(<span>self) ‑> numpy.ndarray</span>
</code></dt>
<dd>
<div class="desc"><p>Rotation about z</p>
</div>
</dd>
</dl>
</dd>
<dt id="anabel.elements.Beam"><code class="flex name class">
<span>class <span class="ident">Beam</span></span>
<span>(</span><span>tag, iNode, jNode, E=None, A=None, I=None, properties=None, **kwds)</span>
</code></dt>
<dd>
<div class="desc"><p>linear 2D Euler-Bernouli frame element</p>
</div>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></li>
<li><a title="anabel.elements.BasicLink" href="#anabel.elements.BasicLink">BasicLink</a></li>
</ul>
<h3>Subclasses</h3>
<ul class="hlist">
<li><a title="anabel.elements.Beam_Column2D" href="#anabel.elements.Beam_Column2D">Beam_Column2D</a></li>
<li><a title="anabel.elements.Beam_Column2D_FL" href="#anabel.elements.Beam_Column2D_FL">Beam_Column2D_FL</a></li>
</ul>
<h3>Class variables</h3>
<dl>
<dt id="anabel.elements.Beam.Qpl"><code class="name">var <span class="ident">Qpl</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam.force_dict"><code class="name">var <span class="ident">force_dict</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam.ndf"><code class="name">var <span class="ident">ndf</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam.ndm"><code class="name">var <span class="ident">ndm</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam.nn"><code class="name">var <span class="ident">nn</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam.nq"><code class="name">var <span class="ident">nq</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam.nv"><code class="name">var <span class="ident">nv</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Instance variables</h3>
<dl>
<dt id="anabel.elements.Beam.A"><code class="name">var <span class="ident">A</span></code></dt>
<dd>
<div class="desc"><p>Cross-sectional area</p>
</div>
</dd>
<dt id="anabel.elements.Beam.E"><code class="name">var <span class="ident">E</span></code></dt>
<dd>
<div class="desc"><p>Young’s modulus of elasticity</p>
</div>
</dd>
<dt id="anabel.elements.Beam.I"><code class="name">var <span class="ident">I</span></code></dt>
<dd>
<div class="desc"><p>Cross-sectional moment of inertia</p>
</div>
</dd>
<dt id="anabel.elements.Beam.enq"><code class="name">var <span class="ident">enq</span></code></dt>
<dd>
<div class="desc"><p>element number of forces, considering deprecation</p>
</div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="anabel.elements.Beam.Elastic_curve"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">Elastic_curve</span></span>(<span>self, x, end_rotations, scale: float = 10, global_coord=False)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam.ag"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">ag</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam.ah"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">ah</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam.bg_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">bg_matrix</span></span>(<span>self, Roption=False)</span>
</code></dt>
<dd>
<div class="desc"><p>return element global static matrix, bg</p>
</div>
</dd>
<dt id="anabel.elements.Beam.f_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">f_matrix</span></span>(<span>self, Roption=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Flexibility matrix of an element.</p>
</div>
</dd>
<dt id="anabel.elements.Beam.k_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">k_matrix</span></span>(<span>self, *args, **kwds)</span>
</code></dt>
<dd>
<div class="desc"><p>return element local stiffness Matrix</p>
</div>
</dd>
<dt id="anabel.elements.Beam.ke_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">ke_matrix</span></span>(<span>self, *args, **kwds)</span>
</code></dt>
<dd>
<div class="desc"><p>return element global stiffness Matrix</p>
</div>
</dd>
<dt id="anabel.elements.Beam.m_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">m_matrix</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam.q0_vector"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">q0_vector</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam.v0_vector"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">v0_vector</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam.κ"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">κ</span></span>(<span>self, k, state=None, form=None)</span>
</code></dt>
<dd>
<div class="desc"><p>Defines element curvature and calculates the resulting end deformations.</p>
</div>
</dd>
</dl>
<h3>Inherited members</h3>
<ul class="hlist">
<li><code><b><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></b></code>:
<ul class="hlist">
<li><code><a title="anabel.elements.Element.Rx_matrix" href="#anabel.elements.BasicLink.Rx_matrix">Rx_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.Ry_matrix" href="#anabel.elements.BasicLink.Ry_matrix">Ry_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.Rz_matrix" href="#anabel.elements.BasicLink.Rz_matrix">Rz_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.compose" href="#anabel.elements.Element.compose">compose</a></code></li>
<li><code><a title="anabel.elements.Element.cs" href="#anabel.elements.BasicLink.cs">cs</a></code></li>
<li><code><a title="anabel.elements.Element.sn" href="#anabel.elements.BasicLink.sn">sn</a></code></li>
</ul>
</li>
</ul>
</dd>
<dt id="anabel.elements.Beam3d"><code class="flex name class">
<span>class <span class="ident">Beam3d</span></span>
<span>(</span><span>tag, iNode, jNode, E, A, Iy, Iz, Gs, Kv)</span>
</code></dt>
<dd>
<div class="desc"><p>Element parent class</p>
<p>3D elastic Bernoulli beam element.</p>
<h2 id="parameters">Parameters</h2>
<dl>
<dt><strong><code>E</code></strong> : <code>float</code></dt>
<dd>Young’s modulus
</dd>
<dt><strong><code>G</code></strong> : <code>float</code></dt>
<dd>Shear modulus
</dd>
<dt><strong><code>A</code></strong> : <code>float</code></dt>
<dd>Cross section area
</dd>
<dt><strong><code>Iy</code></strong> : <code>float</code></dt>
<dd>Moment of inertia, local y-axis
</dd>
<dt><strong><code>Iz</code></strong> : <code>float</code></dt>
<dd>Moment of inertia, local z-axis
</dd>
<dt><strong><code>Kv</code></strong> : <code>float</code></dt>
<dd>Saint-Venant’s torsion constant
</dd>
</dl>
</div>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></li>
<li><a title="anabel.elements.BasicLink" href="#anabel.elements.BasicLink">BasicLink</a></li>
</ul>
<h3>Class variables</h3>
<dl>
<dt id="anabel.elements.Beam3d.force_dict"><code class="name">var <span class="ident">force_dict</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam3d.ndf"><code class="name">var <span class="ident">ndf</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam3d.ndm"><code class="name">var <span class="ident">ndm</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam3d.nn"><code class="name">var <span class="ident">nn</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Beam3d.nv"><code class="name">var <span class="ident">nv</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Instance variables</h3>
<dl>
<dt id="anabel.elements.Beam3d.E"><code class="name">var <span class="ident">E</span></code></dt>
<dd>
<div class="desc"><p>Young’s modulus of elasticity</p>
</div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="anabel.elements.Beam3d.k_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">k_matrix</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"><p>Calculate the stiffness matrix for a 3D elastic Bernoulli beam element.</p>
<h2 id="parameters">Parameters</h2>
<dl>
<dt><strong><code>E</code></strong> : <code>float</code></dt>
<dd>Young’s modulus
</dd>
<dt><strong><code>G</code></strong> : <code>float</code></dt>
<dd>Shear modulus
</dd>
<dt><strong><code>A</code></strong> : <code>float</code></dt>
<dd>Cross section area
</dd>
<dt><strong><code>Iy</code></strong> : <code>float</code></dt>
<dd>Moment of inertia, local y-axis
</dd>
<dt><strong><code>Iz</code></strong> : <code>float</code></dt>
<dd>Moment of inertia, local z-axis
</dd>
<dt><strong><code>Kv</code></strong> : <code>float</code></dt>
<dd>Saint-Venant’s torsion constant
</dd>
</dl>
<p>Returns —–= Kle local beam stiffness matrix (12 x 12)</p>
</div>
</dd>
<dt id="anabel.elements.Beam3d.ke_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">ke_matrix</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Inherited members</h3>
<ul class="hlist">
<li><code><b><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></b></code>:
<ul class="hlist">
<li><code><a title="anabel.elements.Element.Rx_matrix" href="#anabel.elements.BasicLink.Rx_matrix">Rx_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.Ry_matrix" href="#anabel.elements.BasicLink.Ry_matrix">Ry_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.Rz_matrix" href="#anabel.elements.BasicLink.Rz_matrix">Rz_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.compose" href="#anabel.elements.Element.compose">compose</a></code></li>
<li><code><a title="anabel.elements.Element.cs" href="#anabel.elements.BasicLink.cs">cs</a></code></li>
<li><code><a title="anabel.elements.Element.sn" href="#anabel.elements.BasicLink.sn">sn</a></code></li>
</ul>
</li>
</ul>
</dd>
<dt id="anabel.elements.Beam_Column2D"><code class="flex name class">
<span>class <span class="ident">Beam_Column2D</span></span>
<span>(</span><span>tag, iNode, jNode, E=None, A=None, I=None, properties=None, **kwds)</span>
</code></dt>
<dd>
<div class="desc"><p>linear 2D Euler-Bernouli frame element</p>
</div>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="anabel.elements.Beam" href="#anabel.elements.Beam">Beam</a></li>
<li><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></li>
<li><a title="anabel.elements.BasicLink" href="#anabel.elements.BasicLink">BasicLink</a></li>
</ul>
<h3>Class variables</h3>
<dl>
<dt id="anabel.elements.Beam_Column2D.axial_force"><code class="name">var <span class="ident">axial_force</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="anabel.elements.Beam_Column2D.k_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">k_matrix</span></span>(<span>self, axial_force=None)</span>
</code></dt>
<dd>
<div class="desc"><p>Evaluates the 2D beam-column stiffness matrix using a power series expansion</p>
</div>
</dd>
<dt id="anabel.elements.Beam_Column2D.k_matrix_exact"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">k_matrix_exact</span></span>(<span>self, axial_force=None)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Inherited members</h3>
<ul class="hlist">
<li><code><b><a title="anabel.elements.Beam" href="#anabel.elements.Beam">Beam</a></b></code>:
<ul class="hlist">
<li><code><a title="anabel.elements.Beam.A" href="#anabel.elements.Beam.A">A</a></code></li>
<li><code><a title="anabel.elements.Beam.E" href="#anabel.elements.Beam.E">E</a></code></li>
<li><code><a title="anabel.elements.Beam.I" href="#anabel.elements.Beam.I">I</a></code></li>
<li><code><a title="anabel.elements.Beam.Rx_matrix" href="#anabel.elements.BasicLink.Rx_matrix">Rx_matrix</a></code></li>
<li><code><a title="anabel.elements.Beam.Ry_matrix" href="#anabel.elements.BasicLink.Ry_matrix">Ry_matrix</a></code></li>
<li><code><a title="anabel.elements.Beam.Rz_matrix" href="#anabel.elements.BasicLink.Rz_matrix">Rz_matrix</a></code></li>
<li><code><a title="anabel.elements.Beam.bg_matrix" href="#anabel.elements.Beam.bg_matrix">bg_matrix</a></code></li>
<li><code><a title="anabel.elements.Beam.compose" href="#anabel.elements.Element.compose">compose</a></code></li>
<li><code><a title="anabel.elements.Beam.cs" href="#anabel.elements.BasicLink.cs">cs</a></code></li>
<li><code><a title="anabel.elements.Beam.enq" href="#anabel.elements.Beam.enq">enq</a></code></li>
<li><code><a title="anabel.elements.Beam.f_matrix" href="#anabel.elements.Beam.f_matrix">f_matrix</a></code></li>
<li><code><a title="anabel.elements.Beam.ke_matrix" href="#anabel.elements.Beam.ke_matrix">ke_matrix</a></code></li>
<li><code><a title="anabel.elements.Beam.sn" href="#anabel.elements.BasicLink.sn">sn</a></code></li>
<li><code><a title="anabel.elements.Beam.κ" href="#anabel.elements.Beam.κ">κ</a></code></li>
</ul>
</li>
</ul>
</dd>
<dt id="anabel.elements.Beam_Column2D_FL"><code class="flex name class">
<span>class <span class="ident">Beam_Column2D_FL</span></span>
<span>(</span><span>tag, iNode, jNode, E=None, A=None, I=None, properties=None, **kwds)</span>
</code></dt>
<dd>
<div class="desc"><p>linear 2D Euler-Bernouli frame element</p>
</div>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="anabel.elements.Beam" href="#anabel.elements.Beam">Beam</a></li>
<li><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></li>
<li><a title="anabel.elements.BasicLink" href="#anabel.elements.BasicLink">BasicLink</a></li>
</ul>
<h3>Class variables</h3>
<dl>
<dt id="anabel.elements.Beam_Column2D_FL.axial_force"><code class="name">var <span class="ident">axial_force</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="anabel.elements.Beam_Column2D_FL.k_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">k_matrix</span></span>(<span>self, axial_force=None)</span>
</code></dt>
<dd>
<div class="desc"><p>Evaluates the 2D beam-column stiffness matrix using a power series expansion</p>
</div>
</dd>
<dt id="anabel.elements.Beam_Column2D_FL.k_matrix_exact"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">k_matrix_exact</span></span>(<span>self, axial_force=None)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Inherited members</h3>
<ul class="hlist">
<li><code><b><a title="anabel.elements.Beam" href="#anabel.elements.Beam">Beam</a></b></code>:
<ul class="hlist">
<li><code><a title="anabel.elements.Beam.A" href="#anabel.elements.Beam.A">A</a></code></li>
<li><code><a title="anabel.elements.Beam.E" href="#anabel.elements.Beam.E">E</a></code></li>
<li><code><a title="anabel.elements.Beam.I" href="#anabel.elements.Beam.I">I</a></code></li>
<li><code><a title="anabel.elements.Beam.Rx_matrix" href="#anabel.elements.BasicLink.Rx_matrix">Rx_matrix</a></code></li>
<li><code><a title="anabel.elements.Beam.Ry_matrix" href="#anabel.elements.BasicLink.Ry_matrix">Ry_matrix</a></code></li>
<li><code><a title="anabel.elements.Beam.Rz_matrix" href="#anabel.elements.BasicLink.Rz_matrix">Rz_matrix</a></code></li>
<li><code><a title="anabel.elements.Beam.bg_matrix" href="#anabel.elements.Beam.bg_matrix">bg_matrix</a></code></li>
<li><code><a title="anabel.elements.Beam.compose" href="#anabel.elements.Element.compose">compose</a></code></li>
<li><code><a title="anabel.elements.Beam.cs" href="#anabel.elements.BasicLink.cs">cs</a></code></li>
<li><code><a title="anabel.elements.Beam.enq" href="#anabel.elements.Beam.enq">enq</a></code></li>
<li><code><a title="anabel.elements.Beam.f_matrix" href="#anabel.elements.Beam.f_matrix">f_matrix</a></code></li>
<li><code><a title="anabel.elements.Beam.ke_matrix" href="#anabel.elements.Beam.ke_matrix">ke_matrix</a></code></li>
<li><code><a title="anabel.elements.Beam.sn" href="#anabel.elements.BasicLink.sn">sn</a></code></li>
<li><code><a title="anabel.elements.Beam.κ" href="#anabel.elements.Beam.κ">κ</a></code></li>
</ul>
</li>
</ul>
</dd>
<dt id="anabel.elements.Element"><code class="flex name class">
<span>class <span class="ident">Element</span></span>
<span>(</span><span>ndf, ndm, force_dict=None, nodes=None, elem=None, resp=None, proto=None)</span>
</code></dt>
<dd>
<div class="desc"><p>Element parent class</p>
</div>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="anabel.elements.BasicLink" href="#anabel.elements.BasicLink">BasicLink</a></li>
</ul>
<h3>Subclasses</h3>
<ul class="hlist">
<li><a title="anabel.elements.Beam" href="#anabel.elements.Beam">Beam</a></li>
<li><a title="anabel.elements.Beam3d" href="#anabel.elements.Beam3d">Beam3d</a></li>
<li><a title="anabel.elements.PolyRod" href="#anabel.elements.PolyRod">PolyRod</a></li>
<li><a title="anabel.elements.TensorIsoQuad" href="#anabel.elements.TensorIsoQuad">TensorIsoQuad</a></li>
<li><a title="anabel.elements.Truss" href="#anabel.elements.Truss">Truss</a></li>
<li><a title="anabel.elements.Truss3D" href="#anabel.elements.Truss3D">Truss3D</a></li>
</ul>
<h3>Instance variables</h3>
<dl>
<dt id="anabel.elements.Element.force_keys"><code class="name">var <span class="ident">force_keys</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Element.resp"><code class="name">var <span class="ident">resp</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="anabel.elements.Element.compose"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">compose</span></span>(<span>self, **model_params)</span>
</code></dt>
<dd>
<div class="desc"><p>created 2021-03-31</p>
</div>
</dd>
<dt id="anabel.elements.Element.pw_vector"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">pw_vector</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Element.v0_vector"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">v0_vector</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Inherited members</h3>
<ul class="hlist">
<li><code><b><a title="anabel.elements.BasicLink" href="#anabel.elements.BasicLink">BasicLink</a></b></code>:
<ul class="hlist">
<li><code><a title="anabel.elements.BasicLink.Rx_matrix" href="#anabel.elements.BasicLink.Rx_matrix">Rx_matrix</a></code></li>
<li><code><a title="anabel.elements.BasicLink.Ry_matrix" href="#anabel.elements.BasicLink.Ry_matrix">Ry_matrix</a></code></li>
<li><code><a title="anabel.elements.BasicLink.Rz_matrix" href="#anabel.elements.BasicLink.Rz_matrix">Rz_matrix</a></code></li>
<li><code><a title="anabel.elements.BasicLink.cs" href="#anabel.elements.BasicLink.cs">cs</a></code></li>
<li><code><a title="anabel.elements.BasicLink.sn" href="#anabel.elements.BasicLink.sn">sn</a></code></li>
</ul>
</li>
</ul>
</dd>
<dt id="anabel.elements.IntForce"><code class="flex name class">
<span>class <span class="ident">IntForce</span></span>
<span>(</span><span>elem: object, number: int, nature: str = None)</span>
</code></dt>
<dd>
<div class="desc">
</div>
<h3>Instance variables</h3>
<dl>
<dt id="anabel.elements.IntForce.tag"><code class="name">var <span class="ident">tag</span> : str</code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
</dd>
<dt id="anabel.elements.PlaneQuad"><code class="flex name class">
<span>class <span class="ident">PlaneQuad</span></span>
<span>(</span><span>ndf)</span>
</code></dt>
<dd>
<div class="desc">
</div>
<h3>Methods</h3>
<dl>
<dt id="anabel.elements.PlaneQuad.D"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">D</span></span>(<span>self, problem_type=None)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.PlaneQuad.k_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">k_matrix</span></span>(<span>self, u=None)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
</dd>
<dt id="anabel.elements.PolyRod"><code class="flex name class">
<span>class <span class="ident">PolyRod</span></span>
<span>(</span><span>tag, nodes, E, A)</span>
</code></dt>
<dd>
<div class="desc"><p>Element parent class</p>
</div>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></li>
<li><a title="anabel.elements.BasicLink" href="#anabel.elements.BasicLink">BasicLink</a></li>
</ul>
<h3>Class variables</h3>
<dl>
<dt id="anabel.elements.PolyRod.force_dict"><code class="name">var <span class="ident">force_dict</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.PolyRod.ndf"><code class="name">var <span class="ident">ndf</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.PolyRod.ndm"><code class="name">var <span class="ident">ndm</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.PolyRod.nn"><code class="name">var <span class="ident">nn</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.PolyRod.nv"><code class="name">var <span class="ident">nv</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Instance variables</h3>
<dl>
<dt id="anabel.elements.PolyRod.A"><code class="name">var <span class="ident">A</span></code></dt>
<dd>
<div class="desc"><p>cross-sectional areal</p>
</div>
</dd>
<dt id="anabel.elements.PolyRod.E"><code class="name">var <span class="ident">E</span></code></dt>
<dd>
<div class="desc"><p>Young’s modulus of elasticity</p>
</div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="anabel.elements.PolyRod.B"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">B</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.PolyRod.N"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">N</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.PolyRod.displx"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">displx</span></span>(<span>self, U_vector)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.PolyRod.iforcex"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">iforcex</span></span>(<span>self, U_vector)</span>
</code></dt>
<dd>
<div class="desc"><p>Resisting force vector</p>
</div>
</dd>
<dt id="anabel.elements.PolyRod.k_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">k_matrix</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.PolyRod.ke_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">ke_matrix</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.PolyRod.localize"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">localize</span></span>(<span>self, U_vector)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.PolyRod.pw_vector"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">pw_vector</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.PolyRod.strainx"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">strainx</span></span>(<span>self, U_vector)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Inherited members</h3>
<ul class="hlist">
<li><code><b><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></b></code>:
<ul class="hlist">
<li><code><a title="anabel.elements.Element.Rx_matrix" href="#anabel.elements.BasicLink.Rx_matrix">Rx_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.Ry_matrix" href="#anabel.elements.BasicLink.Ry_matrix">Ry_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.Rz_matrix" href="#anabel.elements.BasicLink.Rz_matrix">Rz_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.compose" href="#anabel.elements.Element.compose">compose</a></code></li>
<li><code><a title="anabel.elements.Element.cs" href="#anabel.elements.BasicLink.cs">cs</a></code></li>
<li><code><a title="anabel.elements.Element.sn" href="#anabel.elements.BasicLink.sn">sn</a></code></li>
</ul>
</li>
</ul>
</dd>
<dt id="anabel.elements.TaperedTruss"><code class="flex name class">
<span>class <span class="ident">TaperedTruss</span></span>
<span>(</span><span>tag, iNode, jNode, E=None, A=None, geo='lin', properties=None, **kwds)</span>
</code></dt>
<dd>
<div class="desc"><p>Element parent class</p>
</div>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="anabel.elements.Truss" href="#anabel.elements.Truss">Truss</a></li>
<li><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></li>
<li><a title="anabel.elements.BasicLink" href="#anabel.elements.BasicLink">BasicLink</a></li>
</ul>
<h3>Methods</h3>
<dl>
<dt id="anabel.elements.TaperedTruss.q0_vector"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">q0_vector</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.TaperedTruss.v0_vector"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">v0_vector</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Inherited members</h3>
<ul class="hlist">
<li><code><b><a title="anabel.elements.Truss" href="#anabel.elements.Truss">Truss</a></b></code>:
<ul class="hlist">
<li><code><a title="anabel.elements.Truss.Rx_matrix" href="#anabel.elements.BasicLink.Rx_matrix">Rx_matrix</a></code></li>
<li><code><a title="anabel.elements.Truss.Ry_matrix" href="#anabel.elements.BasicLink.Ry_matrix">Ry_matrix</a></code></li>
<li><code><a title="anabel.elements.Truss.Rz_matrix" href="#anabel.elements.BasicLink.Rz_matrix">Rz_matrix</a></code></li>
<li><code><a title="anabel.elements.Truss.bg_matrix" href="#anabel.elements.Truss.bg_matrix">bg_matrix</a></code></li>
<li><code><a title="anabel.elements.Truss.compose" href="#anabel.elements.Element.compose">compose</a></code></li>
<li><code><a title="anabel.elements.Truss.cs" href="#anabel.elements.BasicLink.cs">cs</a></code></li>
<li><code><a title="anabel.elements.Truss.f_matrix" href="#anabel.elements.Truss.f_matrix">f_matrix</a></code></li>
<li><code><a title="anabel.elements.Truss.iGLstrain" href="#anabel.elements.Truss.iGLstrain">iGLstrain</a></code></li>
<li><code><a title="anabel.elements.Truss.k_matrix" href="#anabel.elements.Truss.k_matrix">k_matrix</a></code></li>
<li><code><a title="anabel.elements.Truss.kg_matrix" href="#anabel.elements.Truss.kg_matrix">kg_matrix</a></code></li>
<li><code><a title="anabel.elements.Truss.sn" href="#anabel.elements.BasicLink.sn">sn</a></code></li>
</ul>
</li>
</ul>
</dd>
<dt id="anabel.elements.TensorIsoQuad"><code class="flex name class">
<span>class <span class="ident">TensorIsoQuad</span></span>
<span>(</span><span>tag, iNode, jNode, E=None, A=None, properties=None, geom='lin')</span>
</code></dt>
<dd>
<div class="desc"><p>Element parent class</p>
</div>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></li>
<li><a title="anabel.elements.BasicLink" href="#anabel.elements.BasicLink">BasicLink</a></li>
</ul>
<h3>Inherited members</h3>
<ul class="hlist">
<li><code><b><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></b></code>:
<ul class="hlist">
<li><code><a title="anabel.elements.Element.Rx_matrix" href="#anabel.elements.BasicLink.Rx_matrix">Rx_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.Ry_matrix" href="#anabel.elements.BasicLink.Ry_matrix">Ry_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.Rz_matrix" href="#anabel.elements.BasicLink.Rz_matrix">Rz_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.compose" href="#anabel.elements.Element.compose">compose</a></code></li>
<li><code><a title="anabel.elements.Element.cs" href="#anabel.elements.BasicLink.cs">cs</a></code></li>
<li><code><a title="anabel.elements.Element.sn" href="#anabel.elements.BasicLink.sn">sn</a></code></li>
</ul>
</li>
</ul>
</dd>
<dt id="anabel.elements.Truss"><code class="flex name class">
<span>class <span class="ident">Truss</span></span>
<span>(</span><span>tag, iNode, jNode, E=None, A=None, geo='lin', properties=None, **kwds)</span>
</code></dt>
<dd>
<div class="desc"><p>Element parent class</p>
</div>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></li>
<li><a title="anabel.elements.BasicLink" href="#anabel.elements.BasicLink">BasicLink</a></li>
</ul>
<h3>Subclasses</h3>
<ul class="hlist">
<li><a title="anabel.elements.TaperedTruss" href="#anabel.elements.TaperedTruss">TaperedTruss</a></li>
</ul>
<h3>Class variables</h3>
<dl>
<dt id="anabel.elements.Truss.Qpl"><code class="name">var <span class="ident">Qpl</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.force_dict"><code class="name">var <span class="ident">force_dict</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.ndf"><code class="name">var <span class="ident">ndf</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.ndm"><code class="name">var <span class="ident">ndm</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.nn"><code class="name">var <span class="ident">nn</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.nq"><code class="name">var <span class="ident">nq</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.nv"><code class="name">var <span class="ident">nv</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="anabel.elements.Truss.B"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">B</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.GLstrain"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">GLstrain</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.N"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">N</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.ag"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">ag</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.bg_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">bg_matrix</span></span>(<span>self, **kwds)</span>
</code></dt>
<dd>
<div class="desc"><p>return element static matrix, <span class="math inline">\(\mathbf{b}_g\)</span></p>
</div>
</dd>
<dt id="anabel.elements.Truss.f_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">f_matrix</span></span>(<span>self, Roption=True)</span>
</code></dt>
<dd>
<div class="desc"><p>return element flexibility matrix, <span class="math inline">\(\mathbf{f}\)</span></p>
</div>
</dd>
<dt id="anabel.elements.Truss.iGLstrain"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">iGLstrain</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"><p>incremental Green-Lagrange strain</p>
</div>
</dd>
<dt id="anabel.elements.Truss.k_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">k_matrix</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"><p>return element local stiffness matrix</p>
</div>
</dd>
<dt id="anabel.elements.Truss.ke_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">ke_matrix</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.kg_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">kg_matrix</span></span>(<span>self, N)</span>
</code></dt>
<dd>
<div class="desc"><p>return element local stiffness matrix</p>
</div>
</dd>
<dt id="anabel.elements.Truss.pw_vector"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">pw_vector</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.q0_vector"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">q0_vector</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss.v0_vector"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">v0_vector</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Inherited members</h3>
<ul class="hlist">
<li><code><b><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></b></code>:
<ul class="hlist">
<li><code><a title="anabel.elements.Element.Rx_matrix" href="#anabel.elements.BasicLink.Rx_matrix">Rx_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.Ry_matrix" href="#anabel.elements.BasicLink.Ry_matrix">Ry_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.Rz_matrix" href="#anabel.elements.BasicLink.Rz_matrix">Rz_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.compose" href="#anabel.elements.Element.compose">compose</a></code></li>
<li><code><a title="anabel.elements.Element.cs" href="#anabel.elements.BasicLink.cs">cs</a></code></li>
<li><code><a title="anabel.elements.Element.sn" href="#anabel.elements.BasicLink.sn">sn</a></code></li>
</ul>
</li>
</ul>
</dd>
<dt id="anabel.elements.Truss3D"><code class="flex name class">
<span>class <span class="ident">Truss3D</span></span>
<span>(</span><span>tag, iNode, jNode, A, E)</span>
</code></dt>
<dd>
<div class="desc"><p>Element parent class</p>
</div>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></li>
<li><a title="anabel.elements.BasicLink" href="#anabel.elements.BasicLink">BasicLink</a></li>
</ul>
<h3>Class variables</h3>
<dl>
<dt id="anabel.elements.Truss3D.force_dict"><code class="name">var <span class="ident">force_dict</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss3D.ndf"><code class="name">var <span class="ident">ndf</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.elements.Truss3D.ndm"><code class="name">var <span class="ident">ndm</span></code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="anabel.elements.Truss3D.bg_matrix"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">bg_matrix</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"><p>return element static matrix, bg - pp. 57</p>
</div>
</dd>
</dl>
<h3>Inherited members</h3>
<ul class="hlist">
<li><code><b><a title="anabel.elements.Element" href="#anabel.elements.Element">Element</a></b></code>:
<ul class="hlist">
<li><code><a title="anabel.elements.Element.Rx_matrix" href="#anabel.elements.BasicLink.Rx_matrix">Rx_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.Ry_matrix" href="#anabel.elements.BasicLink.Ry_matrix">Ry_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.Rz_matrix" href="#anabel.elements.BasicLink.Rz_matrix">Rz_matrix</a></code></li>
<li><code><a title="anabel.elements.Element.compose" href="#anabel.elements.Element.compose">compose</a></code></li>
<li><code><a title="anabel.elements.Element.cs" href="#anabel.elements.BasicLink.cs">cs</a></code></li>
<li><code><a title="anabel.elements.Element.sn" href="#anabel.elements.BasicLink.sn">sn</a></code></li>
</ul>
</li>
</ul>
</dd>
</dl>
</section>
</main>