# MRI Full Course Formula Sheet

_Compact memorization formulas, two lectures per page in the PDF._

## Week 1 - NMR Basics

### Spin

- **Angular momentum:** p = mv,  J = r × p - Rotating charge.
- **Magnetic moment:** μ = γJ - γ gyromagnetic ratio.
- **Quantization:** J_z = ℏm,  m = I,I-1,...,-I - Spin projection.
- **Spin 1/2:** I = 1/2 ⇒ m = ±1/2 - ^1H has two states.
- **Moment projection:** <font color="#B00020">μ_z = γℏm = ±(1/2)γℏ</font> - Along B_0.

### Energy And Resonance

- **Energy:** <font color="#B00020">E_m = -μ_zB_0 = -γℏB_0m</font> - Parallel lower for γ>0.
- **Gap:** ΔE = γℏB_0 = ℏω_0 - Energy splitting.
- **Boltzmann:** n<sub>down</sub>/n<sub>up</sub> = exp(-ΔE/k<sub>B</sub>T) - Population ratio.
- **Polarization:** <font color="#B00020">Δn/n ≈ ΔE/(2k_BT)</font> - For ΔE << kBT.
- **Net M:** M<sub>0</sub> = ∑μ = Δn μ<sub>z</sub>e<sub>z</sub> - Longitudinal M.
- **Scaling:** M_0 ∝ ρ_HB_0/T - Proton density matters.

### Dynamics

- **Torque:** <font color="#B00020">dμ/dt = γ(μ × B)</font> - Precession.
- **Macroscopic:** <font color="#B00020">dM/dt = γ(M × B)</font> - Same law for M.
- **RF:** B_1(t)=B_1cos(ω_0t)e_x=B_L+B_R - Excitation field.
- **Rotating frame:** <font color="#B00020">(dM/dt)_rot=γM×B-ω_0×M =γM×B_eff</font> - Use effective field.
- **Effective field:** B_eff=(B_0-ω/γ)e_z'+B_1,rote_x' - On resonance mostly B1.
- **Flip angle:** α = γ∫B_1,rot(t)dt - RF pulse area.

### Relaxation

- **T2*:** 1/T<sub>2</sub>* = 1/T<sub>2</sub> + γδB - Field inhomogeneity.
- **Bloch x:** dM_x/dt=γ(M_yB_z-M_zB_y) <font color="#B00020">-M_x/T_2</font> - Transverse loss.
- **Bloch y:** dM_y/dt=γ(M_zB_x-M_xB_z) <font color="#B00020">-M_y/T_2</font> - Transverse loss.
- **Bloch z:** dM_z/dt=γ(M_xB_y-M_yB_x) <font color="#B00020">-(M_z-M_0)/T_1</font> - Recovery.

## Week 2 - Image Formation

### Encoding

- **Gradient:** G<sub>i</sub>=∂B<sub>z</sub>/∂i - i=x,y,z.
- **Linear field:** <font color="#B00020">ΔB<sub>z</sub>(x)=G<sub>x</sub> x</font> - Constant slope.
- **Frequency:** ω(r)=γ(B_0+G r) - Position dependent.
- **Readout:** ω(x)=γG<sub>x</sub> x - Frequency encoding.
- **Phase:** φ(y)=γG<sub>y</sub> y T<sub>y</sub> - Phase encoding.
- **K-space:** <font color="#B00020">k(t)=γ∫G(t)dt</font> - Constant G: k=γGt.

### Signal And FT

- **Signal:** <font color="#B00020">s(k<sub>x</sub>,k<sub>y</sub>) ∝ ∑<sub>i,j</sub> ρ(x<sub>i</sub>,y<sub>j</sub>) exp[j(k<sub>x</sub>x<sub>i</sub>+k<sub>y</sub>y<sub>j</sub>)]</font> - FT of object.
- **Image:** ρ(x,y) ∝ ∑<sub>p,q</sub> s(k<sub>x,p</sub>,k<sub>y,q</sub>) exp[-j(k<sub>x,p</sub>x+k<sub>y,q</sub>y)] - Inverse FT.
- **K spacing:** <font color="#B00020">Δk = 2π/FOV = BW / N<sub>x</sub></font> - Nyquist/readout spacing.
- **Pixel:** <font color="#B00020">Δx=FOV_x/N_x</font> - Same in y.
- **Max k:** k_max=π/Δx=πN_x/FOV_x - Resolution.
- **Readout BW:** BW_x=γG_xFOV_x - Angular freq convention.
- **Dwell:** Δt=2π/BW_x,  T_x=N_xΔt - Sampling.

### Slice And Contrast

- **Gradient moment:** k_i=γ∫G_i(t)dt - Gradient area.
- **Slice thickness:** <font color="#B00020">Δz=BW_RF/(γG_z)</font> - RF bandwidth.
- **RF selectivity:** R=BW_RFT_RF - Longer pulse narrower BW.
- **PD contrast:** C∝ρ_A-ρ_B - Long TR.
- **Partial sat.:** C∝ρ<sub>A</sub>[1-exp(-TR/T<sub>1A</sub>)]-ρ<sub>B</sub>[1-exp(-TR/T<sub>1B</sub>)] - T1 weighting.
- **Scan time:** T_scan≈N_phaseTR - One ky line per TR.

## Week 3 - Fast And Parallel Imaging

### Speed, SNR, Resolution

- **Voxel:** ΔV=ΔxΔyΔz - Voxel volume.
- **SNR scaling:** <font color="#B00020">SNR ∝ ΔV√T_scan/√BW</font> - Core tradeoff.
- **Averages:** SNR ∝ √NSA - Repeated scans.
- **Acceleration:** T_scan,R≈T_scan/R - Undersampling.
- **Aliased FOV:** FOV_alias=FOV/R - Phase undersampling.

### Coil Encoding

- **Coil signal:** s<sub>γ</sub>(k)=∫ρ(x)c<sub>γ</sub>(x) exp(ikx) dx - Sensitivity cγ.
- **Matrix model:** <font color="#B00020">s = Eρ + η</font> - Encoding plus noise.
- **Decode:** i = Fs - Reconstruction matrix.
- **SENSE:** ρ̂=(E^HΨ^-1E)^-1E^HΨ^-1s - Optimum SNR inverse.
- **Regularized:** ρ̂=(E^HΨ^-1E+λI)^-1E^HΨ^-1s - Stabilizes ill-conditioning.

### Parallel Limits

- **SENSE SNR:** <font color="#B00020">SNR_SENSE=SNR_full/(√R · g(x))</font> - g-factor penalty.
- **g-factor:** g(x)=√[(E^HE)_ii((E^HE)^-1)_ii] ≥ 1 - Noise amplification.
- **Good coils:** Distinct c_γ(x) ⇒ low g - Separates aliased voxels.
- **Failure:** R > N_coils or poor sensitivities - Underdetermined/ill-conditioned.

## Week 4 - Image Contrast

### Relaxation Contrast

- **T1 recovery:** M<sub>z</sub>(t)=M<sub>0</sub>+[M<sub>z</sub>(0)-M<sub>0</sub>]exp(-t/T<sub>1</sub>) - Longitudinal.
- **After 90°:** M<sub>z</sub>(t)=M<sub>0</sub>[1-exp(-t/T<sub>1</sub>)] - Mz(0)=0.
- **T2 decay:** M<sub>xy</sub>(t)=M<sub>xy</sub>(0)exp(-t/T<sub>2</sub>) - Spin-spin.
- **T2* decay:** M<sub>xy</sub>(t)=M<sub>xy</sub>(0)exp(-t/T<sub>2</sub>*) - GRE/FID.

### Common Signals

- **Spin echo:** <font color="#B00020">S<sub>SE</sub>∝ρ[1-exp(-TR/T<sub>1</sub>)] exp(-TE/T<sub>2</sub>)</font> - T1 by TR, T2 by TE.
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

- **Signal voltage:** <font color="#B00020">U_sig(x)=ωM_xy(x)C(x)ΔV</font> - Receive sensitivity C.
- **Noise power:** P=σ|E|^2ΔV - Sample losses.
- **Noise variance:** <font color="#B00020">Ψ=4k_BTBW R</font> - Johnson-Nyquist.
- **SNR:** SNR=U_sig/U_noise - Image quality.
- **SNR scaling:** SNR∝ΔV√NSA/√BW - Resolution/speed tradeoff.

### Optimization

- **Increase signal:** ↑C, ↑M_xy, ↑ω, ↑ΔV - More voltage.
- **Reduce noise:** ↓BW, ↓T, ↓R_coil - Less thermal noise.
- **Field scaling:** M_0∝B_0,  ω∝B_0 - U_sig roughly grows strongly with B0.
- **Surface coil:** C(x) high near coil - High local SNR.

### Resolution Limits

- **Fourier:** Δx≈π/k_max - Sampling aperture.
- **Relaxation blur:** k* = γGT_2* - Finite T2* filters k-space.
- **Diffusion blur:** x^2≈6DT_acq - Long readouts blur.
- **SoS combine:** I<sub>SoS</sub>=√(∑<sub>c</sub>|I<sub>c</sub>|<sup>2</sup>) - Magnitude coil combine.

## Week 6 - Flow Imaging

### Motion Phase

- **Trajectory:** r(t)=r_0+v(t-t_0)+a(t-t_0)^2/2+... - Moving spin.
- **Phase:** φ=γ∫G(t)r(t)dt - Gradient phase.
- **Moments:** <font color="#B00020">M_n=∫G(t)(t-t_0)^ndt</font> - nth gradient moment.
- **Expansion:** <font color="#B00020">φ=γ[r_0M_0+vM_1+aM_2/2+...]</font> - Position/velocity/acceleration.
- **Bipolar:** M_0=0,  φ≈γvM_1 - Velocity encoding.

### Phase Contrast

- **Encoding:** <font color="#B00020">VENC=π/(γM_1)</font> - Phase reaches ±π.
- **Velocity:** v=(Δφ/π)VENC - Phase difference map.
- **Aliasing:** |v|>VENC ⇒ phase wraps - Set VENC high enough.
- **Flow rate:** <font color="#B00020">Q=∑<sub>i</sub>v<sub>i</sub>ΔA<sub>i</sub></font> - Through-plane flow.
- **Velocity distribution:** s(x,k<sub>v</sub>)=∑ρ(x,v) exp(jk<sub>v</sub>v) - Generalized velocity encoding.

### Hemodynamics

- **Poiseuille:** Q=ΔP/R,  R∝1/d^4 - Diameter dominates.
- **Reynolds:** Re=ρvd/μ - Laminar if Re<~2000.
- **Shear stress:** SS=-μ ∂v/∂r - Wall shear.
- **Contrast agent:** 1/T_1,app=1/T_1+R_1c - Relaxivity model.

## Week 7 - Motion And Artifacts

### Motion Encoding

- **Phase:** <font color="#B00020">φ=γ∫G(t)x(t)dt</font> - All motion artifacts start here.
- **Motion model:** x(t)=x_0+v(t-t_0)+a(t-t_0)^2/2+... - Taylor expansion.
- **Moment nulling:** M_0=0 removes position phase; M_1=0 compensates velocity - Gradient design.
- **Velocity phase:** φ_v=γvM_1 - Residual if M1 nonzero.
- **Velocity spread:** signal ∝ sinc(βγAΔt Δy/2) - Intravoxel dephasing.

### Artifact Rules

- **Intra-TR:** motion during readout/echo ⇒ phase errors and signal loss - Flow, pulsation.
- **Inter-TR:** motion between ky lines ⇒ ghosting/blurring - Respiration/patient.
- **Periodic ghosts:** ghost spacing in phase direction ∝ 1/(f_motionTR) - Regular motion.
- **Random motion:** random ky phase ⇒ diffuse blur - Irregular motion.

### Correction

- **Rigid transform:** R(r,t)=A(t)r+d(t) - Rotation plus translation.
- **Prospective gradients:** G'(t)=A(t)^-TG(t) - Follow anatomy.
- **Phase correction:** φ'(t)=φ(t)-γG(t)·d(t) - Translation compensation.

## Week 8 - fMRI And Diffusion

### BOLD/fMRI

- **T2*:** 1/T<sub>2</sub>*=1/T<sub>2</sub>+γΔB - Static dephasing.
- **Susceptibility:** ΔB≈ΔχB_0 - Blood oxygenation effect.
- **GRE BOLD:** S(TE)=S<sub>0</sub>exp(-TE/T<sub>2</sub>*) - TE near T2*.
- **Small change:** <font color="#B00020">ΔS/S≈-TE·ΔR_2*</font> - R2*=1/T2*.

### Diffusion Physics

- **Fick:** j=-D∇c(r,t) - Diffusion flux.
- **Diffusion eq.:** ∂c/∂t=D∇^2c - Conservation plus Fick.
- **RMS displacement:** R_rms=√(6DΔ) - 3D free diffusion.
- **Einstein:** D≈v^2τ/6 - Random walk.

### DWI/DTI

- **DWI signal:** <font color="#B00020">S(TE,b)=S<sub>0</sub> exp(-TE/T<sub>2</sub>) exp(-bD)</font> - Scalar diffusion.
- **b-value:** <font color="#B00020">b=γ^2G^2δ^2(Δ-δ/3)</font> - PGSE sensitivity.
- **Tensor:** ln(S/S_0)=-b g^TDg - Direction g.
- **MD:** MD=(λ_1+λ_2+λ_3)/3 - Mean diffusivity.
- **FA:** FA=√(3/2) √∑(λ<sub>i</sub>-MD)<sup>2</sup>/√∑λ<sub>i</sub><sup>2</sup> - Anisotropy.

## Week 9 - Advanced Imaging

### General Encoding

- **Data model:** <font color="#B00020">d=Eρ+η</font> - General MRI inverse problem.
- **Cartesian FT:** E=Fourier sampling operator - Standard MRI.
- **Parallel:** E includes coil sensitivities c_γ(r) - SENSE/arrays.
- **Optimal inverse:** ρ̂=(E^HΨ^-1E)^-1E^HΨ^-1d - If well-conditioned.
- **Regularized:** ρ̂=(E^HΨ^-1E+λI)^-1E^HΨ^-1d - For high R.

### Compressed Sensing

- **Sparsity:** x=Φρ has many small/zero coefficients - Sparse transform.
- **Undersampled data:** d_Ω=P_ΩFρ - Sample subset Ω.
- **CS recon:** <font color="#B00020">min_ρ ||Φρ||_1  s.t.  ||Eρ-d||_2≤ε</font> - Sparse recovery.
- **TV:** Φρ=∇ρ ⇒ total variation penalty - Piecewise smooth images.
- **Sampling:** random/incoherent k-space undersampling - Artifacts become noise-like.

### Limits

- **PSF:** PSF(r)=FT^-1{sampling pattern} - Undersampling artifact shape.
- **Acceleration:** higher R needs sparsity + SNR + calibration - No free lunch.
- **Low-rank/dynamics:** suppρ small or temporal basis small - Advanced priors.

## Week 10 - Spectroscopy I

### Chemical Shift

- **Larmor:** ν=-γB_0 [Hz] - Sign by convention.
- **Shift:** <font color="#B00020">δ=(ν-ν_ref)/ν_ref ·10^6 ppm</font> - Field-independent ppm.
- **Hz separation:** <font color="#B00020">Δν=Δδ · ν_ref ·10^-6</font> - Grows with B0.
- **1 ppm:** 1 ppm = ν_ref·10^-6 Hz - 64 Hz at 1.5T for 1H.

### Spectrum

- **FID:** <font color="#B00020">s(t)=A exp(-t/T<sub>2</sub>*) exp(i2πν<sub>A</sub>t)</font> - Single component.
- **Spectrum:** S(ν)=FT{s(t)} - Frequency-domain signal.
- **Lorentzian:** Re S(ν) ∝ T_2* / [1+(2πT_2*(ν-ν_A))^2] - Line shape.
- **Linewidth:** <font color="#B00020">FWHM=1/(πT<sub>2</sub>*)</font> - Shorter T2* broader.
- **Mixture:** s(t)=∑<sub>c</sub>w<sub>c</sub> exp(-t/T<sub>2,c</sub>*) exp(i2πν<sub>c</sub>t) - Superposition.

### Sampling And J

- **Acquisition:** T_acq=Ndt - N samples.
- **Bandwidth:** BW=1/dt - Hz.
- **Resolution:** dν=1/T_acq - Peak spacing.
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

- **Surface coil:** S(r)=B_1(r) sin[γB_1(r)t] - Sensitivity + flip angle.
- **Adiabatic:** |dθ/dt| << γ|B_eff| - Robust inversion/excitation.
- **PRESS/STEAM:** Echo at TE; stimulated echo stores Mz during TM - Voxel selection.
- **Phase cycling:** linear combinations isolate voxel term - Remove unwanted echoes.

### CSI And High Field

- **Shift artifact:** <font color="#B00020">Δx=Δν_CS/(γG)</font> - Chemical shift displacement.
- **Fractional shift:** Δx/Δx_RF=Δν_CS/BW_RF - Use large RF BW.
- **CSI signal:** <font color="#B00020">s(k<sub>x</sub>,k<sub>y</sub>,t)=∭ρ(x,y,Δν) exp[i(k<sub>x</sub>x+k<sub>y</sub>y+2πΔνt)] dxdydΔν</font> - 2 spatial + spectral.
- **CSI recon:** S(x,y,Δν)=FT_tFT_kxFT_ky{s} - 3D transform.
- **CSI scan time:** T_scan=N_xN_yTR·NSA - Slow phase encoding.
- **High-field SNR:** U_sig∼B_0^2, U_noise∼B_0, SNR∼B_0 - Approximate.
- **SAR:** P∝σE^2∝σγ^2B_0^2B_1^2 - High-field cost.
