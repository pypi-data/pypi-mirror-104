---
title: anabel.sections
summary:
template: pdoc.html
...
<main>
<header>
<h1 class="title">Module <code>anabel.sections</code></h1>
</header>
<section id="section-intro">
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="anabel.sections.Composite_Section"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">Composite_Section</span></span>(<span>Y, DY, DZ, quad, y_shift=0.0, mat=None)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.sections.I_Sect"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">I_Sect</span></span>(<span>b, d, alpha, beta, quad, yref=0.0, MatData=None)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.sections.TC_Sect"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">TC_Sect</span></span>(<span>d, bf, tw, quad, yref=0.0, tf=None, ymf=None, MatData=None, **kwds)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.sections.T_Sect"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">T_Sect</span></span>(<span>d, quad, b=None, bf=None, tf=None, tw=None, alpha=None, beta=None, yref=0.0, MatData=None)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.sections.W_Sect"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">W_Sect</span></span>(<span>b, d, alpha, beta, quadf, quadw, yref=0.0, MatData=None)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.sections.ei"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">ei</span></span>(<span>y, epsa, kappa)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.sections.epsi"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">epsi</span></span>(<span>y, epsa, kappa)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
<dt id="anabel.sections.load_aisc"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">load_aisc</span></span>(<span>SectionName, props='')</span>
</code></dt>
<dd>
<div class="desc"><p>Load cross section properties from AISC database.</p>
<p>props: A list of AISC properties, or one of the following: - ‘simple’: <code>A</code>, <code>Ix</code>, <code>Zx</code></p>
</div>
</dd>
<dt id="anabel.sections.section2d"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">section2d</span></span>(<span>yi, dA, nIP, mat, **kwds)</span>
</code></dt>
<dd>
<div class="desc"><p>Generate a section response function</p>
<h2 id="studies">Studies</h2>
</div>
</dd>
</dl>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="anabel.sections.Rectangle"><code class="flex name class">
<span>class <span class="ident">Rectangle</span></span>
<span>(</span><span>b, d, quad=None, yref=0.0, mat=None, **kwds)</span>
</code></dt>
<dd>
<div class="desc"><p>Rectangular cross section</p>
</div>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="anabel.sections.Section" href="#anabel.sections.Section">Section</a></li>
</ul>
</dd>
<dt id="anabel.sections.Section"><code class="flex name class">
<span>class <span class="ident">Section</span></span>
</code></dt>
<dd>
<div class="desc">
</div>
<h3>Subclasses</h3>
<ul class="hlist">
<li><a title="anabel.sections.Rectangle" href="#anabel.sections.Rectangle">Rectangle</a></li>
<li><a title="anabel.sections.Tee" href="#anabel.sections.Tee">Tee</a></li>
</ul>
<h3>Methods</h3>
<dl>
<dt id="anabel.sections.Section.assemble"><code class="sourceCode hljs python name flex">
<span>def <span class="ident">assemble</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc">
</div>
</dd>
</dl>
</dd>
<dt id="anabel.sections.Tee"><code class="flex name class">
<span>class <span class="ident">Tee</span></span>
<span>(</span><span>d=None, quad=None, b=None, bf=None, tf=None, tw=None, alpha=None, beta=None, yref=0.0, mat=None)</span>
</code></dt>
<dd>
<div class="desc">
</div>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="anabel.sections.Section" href="#anabel.sections.Section">Section</a></li>
</ul>
</dd>
</dl>
</section>
</main>