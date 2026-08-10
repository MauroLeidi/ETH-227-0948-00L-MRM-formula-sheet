# MRI Full Course Formula Sheet

_Compact memorization formulas, two lectures per page in the PDF._

## Week 1 - NMR Basics

### Spin

- **Angular momentum:** p = mv,  J = r × p - Rotating charge.
- **Magnetic moment:** μ = γJ - γ gyromagnetic ratio.
- **Quantization:** J<sub>z</sub> = ℏm,  m = I,I-1,...,-I - Spin projection.
- **Spin 1/2:** I = 1/2 ⇒ m = ±1/2 - <sup>1</sup>H has two states.
- **Moment projection:** <font color="#B00020">μ<sub>z</sub> = γℏm = ±(1/2)γℏ</font> - Along B<sub>0</sub>.

### Energy And Resonance

- **Energy:** <font color="#B00020">E<sub>m</sub> = -μ<sub>z</sub>B<sub>0</sub> = -γℏB<sub>0</sub>m</font> - Parallel lower for γ>0.
- **Gap:** ΔE = γℏB<sub>0</sub> = ℏω<sub>0</sub> - Energy splitting.
- **Boltzmann:** n<sub>down</sub>/n<sub>up</sub> = exp(-ΔE/k<sub>B</sub>T) - Population ratio.
- **Polarization:** <font color="#B00020">Δn/n ≈ ΔE/(2k<sub>B</sub>T)</font> - For ΔE << kBT.
- **Net M:** M<sub>0</sub> = ∑μ = Δn μ<sub>z</sub>e<sub>z</sub> - Longitudinal M.
- **Scaling:** M<sub>0</sub> ∝ ρ<sub>H</sub>B<sub>0</sub>/T - Proton density matters.

### Dynamics

- **Torque:** <font color="#B00020">dμ/dt = γ(μ × B)</font> - Precession.
- **Macroscopic:** <font color="#B00020">dM/dt = γ(M × B)</font> - Same law for M.
- **RF:** B<sub>1</sub>(t)=B<sub>1</sub>cos(ω<sub>0</sub>t)e<sub>x</sub>=B<sub>L</sub>+B<sub>R</sub> - Excitation field.
- **Rotating frame:** <font color="#B00020">(dM/dt)<sub>rot</sub>=γM×B-ω<sub>0</sub>×M =γM×B<sub>eff</sub></font> - Use effective field.
- **Effective field:** B<sub>eff</sub>=(B<sub>0</sub>-ω/γ)e<sub>z'</sub>+B<sub>1,rot</sub>e<sub>x'</sub> - On resonance mostly B1.
- **Flip angle:** α = γ∫B<sub>1,rot</sub>(t)dt - RF pulse area.

### Relaxation

- **T2*:** 1/T<sub>2</sub>* = 1/T<sub>2</sub> + γδB - Field inhomogeneity.
- **Bloch x:** dM<sub>x</sub>/dt=γ(M<sub>y</sub>B<sub>z</sub>-M<sub>z</sub>B<sub>y</sub>) <font color="#B00020">-M<sub>x</sub>/T<sub>2</sub></font> - Transverse loss.
- **Bloch y:** dM<sub>y</sub>/dt=γ(M<sub>z</sub>B<sub>x</sub>-M<sub>x</sub>B<sub>z</sub>) <font color="#B00020">-M<sub>y</sub>/T<sub>2</sub></font> - Transverse loss.
- **Bloch z:** dM<sub>z</sub>/dt=γ(M<sub>x</sub>B<sub>y</sub>-M<sub>y</sub>B<sub>x</sub>) <font color="#B00020">-(M<sub>z</sub>-M<sub>0</sub>)/T<sub>1</sub></font> - Recovery.

## Week 2 - Image Formation

### Encoding

- **Gradient:** G<sub>i</sub>=∂B<sub>z</sub>/∂i - i=x,y,z.
- **Loop field:** <font color="#B00020">B<sub>z</sub>(z)=μ<sub>0</sub>I r<sup>2</sup>/(2(r<sup>2</sup>+z<sup>2</sup>)<sup>3/2</sup>)</font> - Circular current loop.
- **Linear field:** <font color="#B00020">ΔB<sub>z</sub>(x)=G<sub>x</sub> x</font> - Constant slope.
- **Frequency:** ω(r)=γ(B<sub>0</sub>+G r) - Position dependent.
- **Readout:** Δω(x)=γG<sub>x</sub> x - Frequency encoding.
- **Phase:** φ(y)=γG<sub>y</sub> y T<sub>y</sub> - Phase encoding.
- **K-space:** <font color="#B00020">k(t)=γ∫G(t)dt</font> - Constant G: k=γGt.

### Signal And FT

- **Signal:** <font color="#B00020">s(k<sub>x</sub>,k<sub>y</sub>) ∝ ∑<sub>i,j</sub> ρ(x<sub>i</sub>,y<sub>j</sub>) exp[j(k<sub>x</sub>x<sub>i</sub>+k<sub>y</sub>y<sub>j</sub>)]</font> - FT of object.
- **Image:** ρ(x,y) ∝ ∑<sub>p,q</sub> s(k<sub>x,p</sub>,k<sub>y,q</sub>) exp[-j(k<sub>x,p</sub>x+k<sub>y,q</sub>y)] - Inverse FT.
- **K spacing:** <font color="#B00020">Δk = 2π/FOV = BW / N<sub>x</sub></font> - Nyquist/readout spacing.
- **Pixel:** <font color="#B00020">Δx=FOV<sub>x</sub>/N<sub>x</sub></font> - Same in y.
- **Max k:** k<sub>max</sub>=π/Δx=πN<sub>x</sub>/FOV<sub>x</sub> - Resolution.
- **Readout BW:** BW<sub>x</sub>=γG<sub>x</sub>FOV<sub>x</sub> - Angular freq convention.
- **Dwell:** Δt=2π/BW<sub>x</sub>,  T<sub>x</sub>=N<sub>x</sub>Δt - Sampling.

### Slice And Contrast

- **Gradient moment:** k<sub>i</sub>=γ∫G<sub>i</sub>(t)dt - Gradient area.
- **Slice thickness:** <font color="#B00020">Δz=BW<sub>RF</sub>/(γG<sub>z</sub>)</font> - RF bandwidth.
- **RF selectivity:** R=BW<sub>RF</sub>T<sub>RF</sub> - Longer pulse narrower BW.
- **PD contrast:** C∝ρ<sub>A</sub>-ρ<sub>B</sub> - Long TR.
- **Partial sat.:** C∝ρ<sub>A</sub>[1-exp(-TR/T<sub>1A</sub>)]-ρ<sub>B</sub>[1-exp(-TR/T<sub>1B</sub>)] - T1 weighting.
- **Scan time:** T<sub>scan</sub>≈N<sub>phase</sub>TR - One ky line per TR.

## Week 3 - Fast And Parallel Imaging

### Speed, SNR, Resolution

- **Voxel:** ΔV=ΔxΔyΔz - Voxel volume.
- **Signal:** <font color="#B00020">u<sub>S</sub>(t)∝ω<sub>0</sub>μ<sub>0</sub>ρ γ<sup>2</sup>ℏ<sup>2</sup>B<sub>0</sub>/(4k<sub>B</sub>T)</font> - Induced voltage.
- **Noise std.:** <font color="#B00020">ψ<sub>u</sub>∝γB<sub>0</sub></font> - Receive noise scale.
- **SNR physical:** <font color="#B00020">SNR=u<sub>S</sub>/ψ<sub>u</sub>∝γ<sup>2</sup>B<sub>0</sub>η∝ΔV√t</font> - Field, coil, voxel, time.
- **SNR scaling:** <font color="#B00020">SNR ∝ ΔV√T<sub>scan</sub>/√BW</font> - Core tradeoff.
- **Averages:** SNR ∝ √NSA - Repeated scans.
- **Acceleration:** T<sub>scan,R</sub>≈T<sub>scan</sub>/R - Undersampling.
- **Aliased FOV:** FOV<sub>alias</sub>=FOV/R - Phase undersampling.

### Coil Encoding

- **Coil signal:** s<sub>γ</sub>(k)=∫ρ(x)c<sub>γ</sub>(x) exp(ikx) dx - Sensitivity cγ.
- **Matrix model:** <font color="#B00020">s = Eρ + η</font> - Encoding plus noise.
- **Decode:** i = Fs,  F E = I (ideal) - E is not directly invertible.
- **Pseudoinverse:** <font color="#B00020">F=(E<sup>H</sup>E)<sup>-1</sup>E<sup>H</sup></font> - Noise ignored.
- **SENSE:** ρ̂=(E<sup>H</sup>Ψ<sup>-1</sup>E)<sup>-1</sup>E<sup>H</sup>Ψ<sup>-1</sup>s - Accounts for non-independent coil noise.
- **Regularized:** ρ̂=(E<sup>H</sup>Ψ<sup>-1</sup>E+λI)<sup>-1</sup>E<sup>H</sup>Ψ<sup>-1</sup>s - Stabilizes ill-conditioning.

### Parallel Limits

- **SENSE SNR:** <font color="#B00020">SNR<sub>SENSE</sub>=SNR<sub>full</sub>/(√R · g(x))</font> - g-factor penalty.
- **g-factor:** g(x)=√[(E<sup>H</sup>E)<sub>ii</sub>((E<sup>H</sup>E)<sup>-1</sup>)<sub>ii</sub>] ≥ 1 - Noise amplification.
- **Good coils:** Distinct c_γ(x) ⇒ low g - Separates aliased voxels.
- **Failure:** R > N<sub>coils</sub> or poor sensitivities - Underdetermined/ill-conditioned.

## Week 4 - Image Contrast

### Relaxation Contrast

- **T1 recovery:** M<sub>z</sub>(t)=M<sub>0</sub>+[M<sub>z</sub>(0)-M<sub>0</sub>]exp(-t/T<sub>1</sub>) - Longitudinal.
- **After 90°:** M<sub>z</sub>(t)=M<sub>0</sub>[1-exp(-t/T<sub>1</sub>)] - Mz(0)=0.
- **T2 decay:** M<sub>xy</sub>(t)=M<sub>xy</sub>(0)exp(-t/T<sub>2</sub>) - Spin-spin.
- **T2* decay:** M<sub>xy</sub>(t)=M<sub>xy</sub>(0)exp(-t/T<sub>2</sub>*) - GRE/FID.
- **Dipolar T1:** <font color="#B00020">1/T<sub>1</sub>=[6ℏ<sup>2</sup>γ<sup>4</sup>/(20r<sup>6</sup>)][J(ω)+4J(2ω)]</font> - Two spins at distance r.
- **Dipolar T2:** <font color="#B00020">1/T<sub>2</sub>=[3ℏ<sup>2</sup>γ<sup>4</sup>/(20r<sup>6</sup>)][3J(0)+5J(ω)+2J(2ω)]</font> - Includes static term J(0).

### Analytical Description

- **Sequence ops:** M<sub>n+1</sub>=O<sub>n</sub>...O<sub>1</sub>M<sub>0</sub>,  O∈{A(α),R(φ)} - RF pulse plus relaxation blocks.
- **RF operator:** <font color="#B00020">A(α)=cosα I+(1−cosα)bb<sup>T</sup>+sinα skew(b)</font> - Rotation around RF axis b.
- **Relax. op.:** <font color="#B00020">M'=R(φ)M+(1−E<sub>1</sub>)M<sub>0</sub>e<sub>z</sub></font> - E<sub>1</sub>=e<sup>−t/T<sub>1</sub></sup>, E<sub>2</sub>=e<sup>−t/T<sub>2</sub></sup>.
- **R matrix:** R(φ)=[E<sub>2</sub>cosφ,−E<sub>2</sub>sinφ,0; E<sub>2</sub>sinφ,E<sub>2</sub>cosφ,0; 0,0,E<sub>1</sub>] - Precession plus decay.

### Common Signals

- **Spin echo:** <font color="#B00020">S<sub>SE</sub>∝ρ[1-exp(-TR/T<sub>1</sub>)] exp(-TE/T<sub>2</sub>)</font> - T1 by TR, T2 by TE.
- **Max contrast TR:** <font color="#B00020">T<sub>R</sub>=[T<sub>1A</sub>T<sub>1B</sub>/(T<sub>1B</sub>-T<sub>1A</sub>)] ln[(S<sub>A</sub>T<sub>1B</sub>)/(S<sub>B</sub>T<sub>1A</sub>)]</font> - Obtained by setting dC/dTR=0.
- **GRE:** S<sub>GRE</sub>∝ρ sinα (1-E<sub>1</sub>)/(1-E<sub>1</sub>cosα) exp(-TE/T<sub>2</sub>*) - E1=exp(-TR/T1).
- **Inversion:** M<sub>z</sub>(TI)=M<sub>0</sub>[1-2exp(-TI/T<sub>1</sub>)] - TR >> T1.
- **Null time:** <font color="#B00020">TI<sub>null</sub> = T<sub>1</sub> ln2</font> - Suppress tissue.
- **Ernst:** <font color="#B00020">α<sub>E</sub>=arccos[exp(-TR/T<sub>1</sub>)]</font> - Max steady-state signal.

### Weighting Rules

- **PD:** TR long, TE short - Minimize relaxation weighting.
- **T1:** TR short, TE short - T1 recovery dominates.
- **T2:** TR long, TE long - T2 decay dominates.
- **T2*:** GRE with TE long - Sensitive to dephasing.

## Week 5 - SNR And Hardware

### Signal And Noise

- **Signal voltage:** <font color="#B00020">U<sub>sig</sub>(x)=ωM<sub>xy</sub>(x)C(x)ΔV</font> - Receive sensitivity C.
- **Noise power:** P=σ|E|<sup>2</sup>ΔV - Sample losses.
- **Noise variance:** <font color="#B00020">Ψ=4k<sub>B</sub>T BW R</font> - Johnson-Nyquist.
- **SNR:** SNR=U<sub>sig</sub>/U<sub>noise</sub> - Image quality.
- **SNR scaling:** SNR∝ΔV√NSA/√BW - Resolution/speed tradeoff.

### Optimization

- **Increase signal:** ↑C, ↑M<sub>xy</sub>, ↑ω, ↑ΔV - More voltage.
- **Reduce noise:** ↓BW, ↓T, ↓R<sub>coil</sub> - Less thermal noise.
- **Field scaling:** M<sub>0</sub>∝B<sub>0</sub>,  ω∝B<sub>0</sub> - U<sub>sig</sub> roughly grows strongly with B0.
- **Surface coil:** C(x) high near coil - High local SNR.

### Resolution Limits

- **Fourier:** Δx≈π/k<sub>max</sub> - Sampling aperture.
- **Relaxation blur:** k* = γGT<sub>2</sub>* - Finite T2* filters k-space.
- **Diffusion blur:** x<sup>2</sup>≈6DT<sub>acq</sub> - Long readouts blur.
- **SoS combine:** I<sub>SoS</sub>=√(∑<sub>c</sub>|I<sub>c</sub>|<sup>2</sup>) - Magnitude coil combine.

## Week 6 - Flow Imaging

### Motion Phase

- **Trajectory:** r(t)=r<sub>0</sub>+v(t-t<sub>0</sub>)+a(t-t<sub>0</sub>)<sup>2</sup>/2+... - Moving spin.
- **Phase:** φ=γ∫G(t)r(t)dt - Gradient phase.
- **Moments:** <font color="#B00020">M<sub>n</sub>=∫G(t)(t-t<sub>0</sub>)<sup>n</sup>dt</font> - nth gradient moment.
- **Expansion:** <font color="#B00020">φ=γ[r<sub>0</sub>M<sub>0</sub>+vM<sub>1</sub>+aM<sub>2</sub>/2+...]</font> - Position/velocity/acceleration.
- **Bipolar:** M<sub>0</sub>=0,  φ≈γvM<sub>1</sub> - Velocity encoding.

### Phase Contrast

- **Encoding:** <font color="#B00020">VENC=π/(γM<sub>1</sub>)</font> - Phase reaches ±π.
- **Velocity:** v=(Δφ/π)VENC - Phase difference map.
- **Aliasing:** |v|>VENC ⇒ phase wraps - Set VENC high enough.
- **Flow rate:** <font color="#B00020">Q=∑<sub>i</sub>v<sub>i</sub>ΔA<sub>i</sub></font> - Through-plane flow.
- **Velocity distribution:** s(x,k<sub>v</sub>)=∑ρ(x,v) exp(jk<sub>v</sub>v) - Generalized velocity encoding.

### Hemodynamics

- **Poiseuille:** Q=ΔP/R,  R∝1/d<sup>4</sup> - Diameter dominates.
- **Reynolds:** Re=ρvd/μ - Laminar if Re<~2000.
- **Shear stress:** SS=-μ ∂v/∂r - Wall shear.
- **Contrast agent:** 1/T<sub>1,app</sub>=1/T<sub>1</sub>+R<sub>1</sub>c - Relaxivity model.

## Week 7 - Motion And Artifacts

### Motion Encoding

- **Phase:** <font color="#B00020">φ=γ∫G(t)x(t)dt</font> - All motion artifacts start here.
- **Motion model:** x(t)=x<sub>0</sub>+v(t-t<sub>0</sub>)+a(t-t<sub>0</sub>)<sup>2</sup>/2+... - Taylor expansion.
- **Moment nulling:** M<sub>0</sub>=0 removes position phase; M<sub>1</sub>=0 compensates velocity - Gradient design.
- **Velocity phase:** φ<sub>v</sub>=γvM<sub>1</sub> - Residual if M1 nonzero.
- **Velocity spread:** signal ∝ sinc(βγAΔt Δy/2) - Intravoxel dephasing.

### Artifact Rules

- **Intra-TR:** motion during readout/echo ⇒ phase errors and signal loss - Flow, pulsation.
- **Inter-TR:** motion between ky lines ⇒ ghosting/blurring - Respiration/patient.
- **Periodic ghosts:** ghost spacing in phase direction ∝ 1/(f<sub>motion</sub>TR) - Regular motion.
- **Random motion:** random ky phase ⇒ diffuse blur - Irregular motion.

### Correction

- **Rigid transform:** R(r,t)=A(t)r+d(t) - Rotation plus translation.
- **Prospective gradients:** G'(t)=A(t)<sup>-T</sup>G(t) - Follow anatomy.
- **Phase correction:** φ'(t)=φ(t)-γG(t)·d(t) - Translation compensation.

## Week 8 - fMRI And Diffusion

### BOLD/fMRI

- **T2*:** 1/T<sub>2</sub>*=1/T<sub>2</sub>+γΔB - Static dephasing.
- **Susceptibility:** ΔB≈ΔχB<sub>0</sub> - Blood oxygenation effect.
- **GRE BOLD:** S(TE)=S<sub>0</sub>exp(-TE/T<sub>2</sub>*) - TE near T2*.
- **Small change:** <font color="#B00020">ΔS/S≈-TE·ΔR<sub>2</sub>*</font> - R2*=1/T2*.

### Diffusion Physics

- **Fick:** j=-D∇c(r,t) - Diffusion flux.
- **Diffusion eq.:** ∂c/∂t=D∇<sup>2</sup>c - Conservation plus Fick.
- **RMS displacement:** R<sub>rms</sub>=√(6DΔ) - 3D free diffusion.
- **Einstein:** D≈v<sup>2</sup>τ/6 - Random walk.

### DWI/DTI

- **DWI signal:** <font color="#B00020">S(TE,b)=S<sub>0</sub> exp(-TE/T<sub>2</sub>) exp(-bD)</font> - Scalar diffusion.
- **b-value:** <font color="#B00020">b=γ<sup>2</sup>G<sup>2</sup>δ<sup>2</sup>(Δ-δ/3)</font> - PGSE sensitivity.
- **Tensor:** ln(S/S<sub>0</sub>)=-b g<sup>T</sup>Dg - Direction g.
- **MD:** MD=(λ<sub>1</sub>+λ<sub>2</sub>+λ<sub>3</sub>)/3 - Mean diffusivity.
- **FA:** FA=√(3/2) √∑(λ<sub>i</sub>-MD)<sup>2</sup>/√∑λ<sub>i</sub><sup>2</sup> - Anisotropy.

## Week 9 - Advanced Imaging

### General Encoding

- **Data model:** <font color="#B00020">d=Eρ+η</font> - General MRI inverse problem.
- **Cartesian FT:** E=Fourier sampling operator - Standard MRI.
- **Parallel:** E includes coil sensitivities c<sub>γ</sub>(r) - SENSE/arrays.
- **Optimal inverse:** ρ̂=(E<sup>H</sup>Ψ<sup>-1</sup>E)<sup>-1</sup>E<sup>H</sup>Ψ<sup>-1</sup>d - If well-conditioned.
- **Regularized:** ρ̂=(E<sup>H</sup>Ψ<sup>-1</sup>E+λI)<sup>-1</sup>E<sup>H</sup>Ψ<sup>-1</sup>d - For high R.

### Compressed Sensing

- **Sparsity:** x=Φρ has many small/zero coefficients - Sparse transform.
- **Undersampled data:** d<sub>Ω</sub>=P<sub>Ω</sub>Fρ - Sample subset Ω.
- **CS recon:** <font color="#B00020">min<sub>ρ</sub> ||Φρ||<sub>1</sub>  s.t.  ||Eρ-d||<sub>2</sub>≤ε</font> - Sparse recovery.
- **TV:** Φρ=∇ρ ⇒ total variation penalty - Piecewise smooth images.
- **Sampling:** random/incoherent k-space undersampling - Artifacts become noise-like.

### Limits

- **PSF:** PSF(r)=FT<sup>-1</sup>{sampling pattern} - Undersampling artifact shape.
- **Acceleration:** higher R needs sparsity + SNR + calibration - No free lunch.
- **Low-rank/dynamics:** suppρ small or temporal basis small - Advanced priors.

## Week 10 - Spectroscopy I

### Chemical Shift

- **Larmor:** ν=-γB<sub>0</sub> [Hz] - Sign by convention.
- **Shift:** <font color="#B00020">δ=(ν-ν<sub>ref</sub>)/ν<sub>ref</sub> ·10<sup>6</sup> ppm</font> - Field-independent ppm.
- **Hz separation:** <font color="#B00020">Δν=Δδ · ν<sub>ref</sub> ·10<sup>-6</sup></font> - Grows with B0.
- **1 ppm:** 1 ppm = ν<sub>ref</sub>·10<sup>-6</sup> Hz - 64 Hz at 1.5T for 1H.

### Spectrum

- **FID:** <font color="#B00020">s(t)=A exp(-t/T<sub>2</sub>*) exp(i2πν<sub>A</sub>t)</font> - Single component.
- **Spectrum:** S(ν)=FT{s(t)} - Frequency-domain signal.
- **Lorentzian:** Re S(ν) ∝ T<sub>2</sub>* / [1+(2πT<sub>2</sub>*(ν-ν<sub>A</sub>))<sup>2</sup>] - Line shape.
- **Linewidth:** <font color="#B00020">FWHM=1/(πT<sub>2</sub>*)</font> - Shorter T2* broader.
- **Mixture:** s(t)=∑<sub>c</sub>w<sub>c</sub> exp(-t/T<sub>2,c</sub>*) exp(i2πν<sub>c</sub>t) - Superposition.

### Sampling And J

- **Acquisition:** T<sub>acq</sub>=Ndt - N samples.
- **Bandwidth:** BW=1/dt - Hz.
- **Resolution:** dν=1/T<sub>acq</sub> - Peak spacing.
- **Resolve peaks:** dν ≤ Δν/2 - Rule of thumb.
- **J multiplet:** N coupled spin-I nuclei ⇒ 2NI+1 lines - Binomial intensities.
- **J echo:** TE=n/J - Odd n flips doublet sign.
- **Editing:** TE=1/J - Difference editing.

## Week 11 - Spectroscopy II

### Suppression And Inversion

- **Water/fat:** Δδ≈3.5 ppm - Water 4.7, fat 1.2 ppm.
- **Phase accrual:** Δφ=2πΔντ - Chemical shift phase.
- **Binomial spacing:** τ≈1/(2Δν) or 1/(4Δν) - Depends on target phase.
- **Inversion recovery:** M<sub>z</sub>(TI)=M<sub>0</sub>[1-2exp(-TI/T<sub>1</sub>)] - After 180°.
- **Null:** <font color="#B00020">TI<sub>null</sub> = T<sub>1</sub> ln2</font> - Water/fat suppression.

### Localization

- **Surface coil:** S(r)=B<sub>1</sub>(r) sin[γB<sub>1</sub>(r)t] - Sensitivity + flip angle.
- **Adiabatic:** |dθ/dt| << γ|B<sub>eff</sub>| - Robust inversion/excitation.
- **PRESS/STEAM:** Echo at TE; stimulated echo stores Mz during TM - Voxel selection.
- **Phase cycling:** linear combinations isolate voxel term - Remove unwanted echoes.

### CSI And High Field

- **Shift artifact:** <font color="#B00020">Δx=Δν<sub>CS</sub>/(γG)</font> - Chemical shift displacement.
- **Fractional shift:** Δx/Δx<sub>RF</sub>=Δν<sub>CS</sub>/BW<sub>RF</sub> - Use large RF BW.
- **CSI signal:** <font color="#B00020">s(k<sub>x</sub>,k<sub>y</sub>,t)=∭ρ(x,y,Δν) exp[i(k<sub>x</sub>x+k<sub>y</sub>y+2πΔνt)] dxdydΔν</font> - 2 spatial + spectral.
- **CSI recon:** S(x,y,Δν)=FT<sub>t</sub>FT<sub>kx</sub>FT<sub>ky</sub>{s} - 3D transform.
- **CSI scan time:** T<sub>scan</sub>=N<sub>x</sub>N<sub>y</sub>TR·NSA - Slow phase encoding.
- **High-field SNR:** U<sub>sig</sub>∼B<sub>0</sub><sup>2</sup>, U<sub>noise</sub>∼B<sub>0</sub>, SNR∼B<sub>0</sub> - Approximate.
- **SAR:** P∝σE<sup>2</sup>∝σγ<sup>2</sup>B<sub>0</sub><sup>2</sup>B<sub>1</sub><sup>2</sup> - High-field cost.
