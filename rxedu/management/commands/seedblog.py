from django.core.management.base import BaseCommand
from rxedu.models import BlogPost
from users.models import User
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds initial blog posts for RxEdu'

    def handle(self, *args, **options):
        # Get admin user as author
        admin = User.objects.filter(is_staff=True).first()
        
        if not admin:
            self.stdout.write(self.style.ERROR('No admin user found. Create one first.'))
            return

        # Blog Post Content
        title = "The Importance of Reusing Leftover Medicine for a Good Cause"
        content = """<h2>Why Medicine Donation Matters in India</h2>

<p>Every year, Indian households discard <strong>medicines worth thousands of crores</strong> simply because they remain unused after treatment. Meanwhile, millions of economically disadvantaged families struggle to afford basic healthcare. <strong>Medicine donation</strong> and <strong>leftover medicine reuse</strong> bridge this critical gap, transforming surplus into life-saving resources.</p>

<p>At <a href="/">RxReuse</a>, we believe that <strong>where sharing becomes healing</strong>, communities thrive. This comprehensive guide explores why donating unused medicines is not just charitable—it's essential for building a healthier, more equitable India.</p>

<h2>The Alarming Scale of Medicine Wastage</h2>

<p>According to recent studies, nearly <strong>20-30% of prescribed medicines</strong> in India go unused. This happens due to:</p>

<ul>
<li>Incomplete treatment courses (patients feel better and stop medication)</li>
<li>Changed prescriptions by doctors</li>
<li>Bulk purchases during emergencies</li>
<li>Leftover antibiotics and chronic disease medications</li>
</ul>

<p>When these <strong>surplus medicines</strong> are thrown in regular trash, they contaminate soil and water sources, creating <a href="https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/pharmaceutical-waste" target="_blank" rel="noopener">pharmaceutical pollution</a> that harms ecosystems. <strong>Medicine recycling through donation</strong> offers an eco-friendly alternative while serving humanity.</p>

<h2>How Medicine Donation Saves Lives</h2>

<p>The cost of healthcare in India remains a significant burden. A family earning ₹15,000 monthly cannot afford ₹3,000 worth of diabetes or blood pressure medications. This is where <strong>free medicine redistribution programs</strong> like RxReuse make a tangible difference.</p>

<p>When you <a href="/inventory/donate/">donate your unused medicines</a>, you enable:</p>

<ul>
<li><strong>Affordable Healthcare Access:</strong> Patients get verified, safe medicines at zero cost</li>
<li><strong>Prevention of Treatment Gaps:</strong> No one skips medications due to financial constraints</li>
<li><strong>Community Health Improvement:</strong> Healthier individuals contribute to healthier neighborhoods</li>
<li><strong>Reduced Medicine Wastage:</strong> Every donated tablet finds purpose instead of polluting landfills</li>
</ul>

<h2>The RxReuse Medicine Donation Model</h2>

<p>Our <strong>medicine bank</strong> operates on transparency and safety. Here's how <strong>leftover medicine donation</strong> works:</p>

<ol>
<li><strong>Donor Registration:</strong> List your surplus, unexpired medicines online with clear photos</li>
<li><strong>Volunteer Verification:</strong> Trained volunteers inspect authenticity, expiry dates, and packaging integrity</li>
<li><strong>Patient Matching:</strong> Verified beneficiaries with prescriptions receive matched medicines</li>
<li><strong>Free Distribution:</strong> Patients pay only minimal shipping charges, making treatment truly affordable</li>
</ol>

<p>This <a href="/community/transparency/">transparent system</a> ensures every donated medicine reaches genuine patients, creating measurable impact you can track.</p>

<h2>Environmental Benefits of Medicine Reuse</h2>

<p>Beyond social impact, <strong>medicine donation</strong> addresses critical environmental concerns. According to the <a href="https://www.who.int/news-room/fact-sheets/detail/pharmaceuticals-in-drinking-water" target="_blank" rel="noopener">World Health Organization</a>, improper pharmaceutical disposal contaminates water supplies, affecting aquatic life and potentially entering the human food chain.</p>

<p>By participating in <strong>medicine redistribution programs</strong>, you:</p>

<ul>
<li>Prevent toxic chemical leaching into groundwater</li>
<li>Reduce pharmaceutical residue in rivers and lakes</li>
<li>Support sustainable healthcare practices</li>
<li>Contribute to India's environmental protection goals</li>
</ul>

<h2>Which Medicines Can You Donate?</h2>

<p>Our <strong>medicine donation platform</strong> accepts:</p>

<ul>
<li><strong>Tablets & Capsules:</strong> Antibiotics, painkillers, vitamins (unopened strips preferred)</li>
<li><strong>Chronic Disease Medications:</strong> Diabetes, hypertension, thyroid medicines</li>
<li><strong>Syrups & Suspensions:</strong> Unopened, unexpired bottles</li>
<li><strong>Injections & Insulin:</strong> Properly stored, with valid expiry dates</li>
</ul>

<p><strong>Important:</strong> We do not accept narcotics, controlled substances, or expired medications. All donations must have at least 6 months validity remaining.</p>

<h2>Real Impact: Numbers That Matter</h2>

<p>Since our inception, RxReuse has:</p>

<ul>
<li>Facilitated <strong>10,000+ medicine donations</strong> across India</li>
<li>Impacted <strong>5,000+ patient lives</strong> with free treatment access</li>
<li>Prevented ₹<strong>50 lakhs worth of medicine wastage</strong></li>
<li>Built a community of <strong>compassionate donors</strong> committed to healthcare equity</li>
</ul>

<p>Read inspiring <a href="/community/stories/">success stories</a> from beneficiaries whose lives transformed through your generosity.</p>

<h2>How You Can Start Donating Today</h2>

<p>Making a difference is simple. <a href="/inventory/donate/">Register your unused medicines</a> in three easy steps:</p>

<ol>
<li><strong>Sign Up:</strong> Create a free account on RxReuse</li>
<li><strong>List Medicines:</strong> Upload details with clear photos and expiry dates</li>
<li><strong>Ship & Track:</strong> Pack safely, ship to our warehouse, and track your donation impact</li>
</ol>

<p>Every contribution matters. That leftover antibiotic course in your cabinet could be a child's cure. Your unused diabetes tablets could be a senior citizen's lifeline.</p>

<h2>Join India's Medicine Sharing Movement</h2>

<p><strong>Medicine donation</strong> is more than charity—it's community-driven healthcare transformation. By choosing to <strong>reuse leftover medicines</strong> through verified platforms like RxReuse, you actively participate in building a healthier, more equitable India.</p>

<p>Don't let surplus medicines waste away. <a href="/inventory/donate/">Donate today</a> and experience the profound joy of saving lives through simple acts of sharing. Together, we prove that <strong>where sharing becomes healing</strong>, everyone wins.</p>

<p><em>Ready to make a difference? <a href="/inventory/donate/">Start your medicine donation journey now</a> or <a href="/aid/">apply for free medicines if you need assistance</a>.</em></p>"""

        # Check if post already exists
        slug = slugify(title)
        if BlogPost.objects.filter(slug=slug).exists():
            self.stdout.write(self.style.WARNING(f'Blog post "{title}" already exists'))
            return

        # Create blog post
        blog_post = BlogPost.objects.create(
            title=title,
            slug=slug,
            author=admin,
            content=content,
            is_published=True
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully created blog post: "{title}"'))
