import type { GetStaticProps } from "next";
import { join } from "path";
import fs from "fs";
import matter from "gray-matter";
import Link from "next/link";

interface PostProps {
  title: string;
  content: string;
  isProtected: boolean;
  slug: string;
}

interface PostList {
  posts: PostProps[];
}

const postsDirectory = join(process.cwd(), "_posts");

const Home = (posts: PostList) => {
  const postList = posts.posts.map((post) => {
    return (
      <li key={post.title}>
        <a className="underline text-blue-600 hover:text-blue-800 visited:text-purple-600">
          <Link
            href={`/${post.isProtected ? "protected" : "open"}/${post.slug}`}
          >
            {post.title}
          </Link>
        </a>
      </li>
    );
  });

  return (
    <div className="flex flex-col">
      <div className="mx-auto">
        <h1 className="text-3xl font-bold underline">Blog!</h1>
        <p>This is my new blog, check out some of the posts below!</p>
        <h2 className="text-2xl font-bold underline">Posts</h2>
        <ul>{postList}</ul>
      </div>
    </div>
  );
};

export const getStaticProps: GetStaticProps<PostList> = async (context) => {
  const files = fs.readdirSync(postsDirectory);

  const posts = files.map((post) => {
    const path = join(process.cwd(), "_posts", post);
    const fileContents = fs.readFileSync(path);

    const { data } = matter(fileContents);
    return {
      title: data["title"],
      content: "",
      isProtected: data["protected"],
      slug: path.replace(/\.md$/, "").split("/").at(-1) || "",
    };
  });

  return {
    props: {
      posts: posts,
    },
  };
};

export default Home;
