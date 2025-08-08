import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  	distDir: 'build',
	rewrites: async () => {
		return [
			{
				source: '/api/:path*',
				destination: `http://${process.env.API_HOST}:${process.env.API_PORT}/api/v1/:path*`
			}
		]
	}
};

export default nextConfig;
